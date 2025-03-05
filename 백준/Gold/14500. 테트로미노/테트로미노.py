# 테트로미노
# 골드 4

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = -1


def cyan():
    global graph, n, m, answer

    # 그냥 옮긴거
    for x in range(n):
        for y in range(m-3):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x][y+3])

    # 회전
    for x in range(n-3):
        for y in range(m):
            answer = max(answer, graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 3][y])

    # 대칭
    # 얘는 대칭이 없음


def yellow():
    global graph, n, m, answer
    # 그냥 옮긴거
    for x in range(n-1):
        for y in range(m-1):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x][y+1]+graph[x+1][y+1])
    # 얘는 회전이랑 대칭이 없구나


def orange():
    global graph, n, m, answer
    # 그냥 옮기기
    for x in range(n-2):
        for y in range(m - 1):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+2][y+1])

    # 회전
    # 1
    for x in range(n-1):
        for y in range(m-2):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x+1][y+2])

    # 2
    for x in range(n-2):
        for y in range(m-1):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x+1][y+1]+graph[x+2][y+1])
    # 3
    for x in range(n-1):
        for y in range(m-2):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x][y+1]+graph[x][y+2])

    # 대칭
    # 4
    for x in range(2, n):
        for y in range(m-1):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x-1][y+1]+graph[x-2][y+1])

    # 5
    for x in range(n-1):
        for y in range(m-2):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+1][y+2])

    # 6
    for x in range(1, n):
        for y in range(m - 2):
            answer = max(answer, graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x - 1][y + 2])

    # 7
    for x in range(n-2):
        for y in range(m-1):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x][y+1])


def green():
    global graph, n, m, answer
    # 그냥 옮기기
    for x in range(n - 2):
        for y in range(m - 1):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+2][y+1])

    # 회전
    # 1
    for x in range(1, n):
        for y in range(m - 2):
            answer = max(answer, graph[x][y] + graph[x][y + 1] + graph[x - 1][y + 1] + graph[x - 1][y + 2])

    # 대칭
    # 2
    for x in range(n - 1):
        for y in range(m - 2):
            answer = max(answer, graph[x][y] + graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 1][y + 2])

    # 3
    # right top
    for x in range(n - 2):
        for y in range(1, m):
            answer = max(answer, graph[x][y] + graph[x + 1][y] + graph[x + 1][y - 1] + graph[x + 2][y - 1])


def purple():
    global graph, n, m, answer
    # 그냥 옮기기
    for x in range(n - 1):
        for y in range(m - 2):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x+1][y+1])

    # 회전
    # 1
    for x in range(n - 2):
        for y in range(m - 1):
            answer = max(answer, graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+2][y])

    # 2
    for x in range(1, n):
        for y in range(m - 2):
            answer = max(answer, graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x-1][y+1])

    # 3
    for x in range(n - 2):
        for y in range(1, m):
            answer = max(answer, graph[x][y] + graph[x + 1][y] + graph[x + 1][y - 1] + graph[x + 2][y])

    # 대칭 없고


cyan()
yellow()
orange()
green()
purple()

print(answer)