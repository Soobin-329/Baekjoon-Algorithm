# 상어 중학교
# 골드 2


import copy
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0


def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False] * n for _ in range(n)]
    color = graph[x][y]
    num_block, num_rainbow, sx, sy = 0, 0, 99, 99

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        cx, cy = queue.popleft()

        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        num_block += 1

        if graph[cx][cy] == 0:
            num_rainbow += 1
        else:
            # 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록,열의 번호가 가장 작은 블록
            sx = min(cx, sx)
            sy = min(cy, sy)

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] in (color, 0):
                    queue.append((nx, ny))

    return num_block, num_rainbow, (sx, sy), visited


def find_group():
    max_group = (0,0,(99,99), []) # num_blocks, num_rainbow, standard_block_position, visited

    for x in range(n):
        for y in range(n):
            # 방문하지 않았고, 일반 블록이라면 블록 그룹 찾기 시작
            if graph[x][y] not in (-1, 0, 9):
                num_block, num_rainbow, standard_block, visited = bfs(x, y)

                max_block, max_rainbow, max_standard_block, max_visited = max_group
                if num_block > max_block:
                    max_group = (num_block, num_rainbow, standard_block, visited)
                elif num_block == max_block:
                    if num_rainbow > max_rainbow:
                        max_group = (num_block, num_rainbow, standard_block, visited)
                    elif num_rainbow == max_rainbow:
                        sx, sy = standard_block
                        mx, my = max_standard_block
                        if sx > mx:
                            max_group = (num_block, num_rainbow, standard_block, visited)
                        elif sx == mx:
                            if sy > my:
                                max_group = (num_block, num_rainbow, standard_block, visited)
    return max_group[0], max_group[3]


def remove_group(visited):
    global graph

    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                # 빈 곳은 9
                graph[x][y] = 9


def gravity():
    global graph
    # 아래 행부터 위로 올라가며 블럭을 기준이 되는 empty row까지 내림
    for col in range(n):
        empty_row = n - 1
        for row in range(n-1, -1, -1):
            if graph[row][col] == -1:
                empty_row = row - 1

            elif graph[row][col] != 9:
                if empty_row != row:
                    graph[empty_row][col] = graph[row][col]
                    graph[row][col] = 9
                    empty_row -= 1
                else:
                    empty_row = row - 1


def rotate_left_90():
    global graph
    columns = list(zip(*graph))[::-1]
    new_board = []
    for row in columns:
        new_board.append(list(row))

    graph = new_board


while True:
    # 블록 그룹 찾기
    size_of_group, block_group_graph = find_group()

    if size_of_group < 2:
        break

    # 블록 그룹의 모든 블록 제거, 점수 올리기
    answer += size_of_group**2
    remove_group(block_group_graph)

    # 중력
    gravity()

    # 90도 반시계 방향 회전
    rotate_left_90()


    # 중력
    gravity()


print(answer)