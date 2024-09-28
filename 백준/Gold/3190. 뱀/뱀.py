# 뱀
# 골드 4


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
# 몸길이
length = 1
# 생존한 시간
count = 0
# 행보를 저장하는 큐
queue = deque()

# 아무것도 없는거는 0
# 뱀은 1
graph = [ [0 for _ in range(n)] for _ in range(n)]
graph[0][0] = 1
# 현재 뱀의 머리 위치
cx, cy = 0, 0
# 현재 뱀의 진행방향
# 오른쪽으로 가면 index + 1, 왼쪽으로 가면 index - 1
directions = [(0,1), (1,0), (0, -1), (-1, 0)]
di = 0

for i in range(k):
    a, b = map(int, input().split())
    # 사과는 4
    graph[a - 1][b - 1] = 4

l = int(input())
# [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
turns = []

for _ in range(l):
    a, b = input().split()
    turns.append([int(a), b])

while True:
    # 방향을 트는지 확인
    if len(turns) > 0 and turns[0][0] == count:
        if turns[0][1] == 'D':
            di += 1
            if di == 4:
                di = 0
        else:
            di -= 1
            if di == -1:
                di = 3
        del turns[0]

    nx = cx + directions[di][0]
    ny = cy + directions[di][1]


    # 벽에 부딪히는가
    if nx < 0 or ny < 0 or ny >= n or nx >= n:
        break

    # 자기 몸에 부딪히는가
    if graph[nx][ny] == 1:
        break

    # 문제가 없다면 사과가 있는지 확인
    # 사과가 있다면 몸길이가 늘어나므로 0이되는 곳이 없다
    if graph[nx][ny] == 4:
        length += 1
        queue.append((cx, cy))

    #  이번에는 사과를 먹지 않았지만
    #  사과를 먹은적 있으면 queue에 행보 추가
    # 그리고 꼬리가 있던 자리는 0이 됨
    elif length > 1:
        queue.append((cx, cy))
        prevx, prevy = queue.popleft()
        graph[prevx][prevy] = 0

    else:
        graph[cx][cy] = 0

    graph[nx][ny] = 1
    cx, cy = nx, ny
    count += 1

count += 1
print(count)