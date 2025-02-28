# 감시
# 골드 3


import sys
input = sys.stdin.readline


def one(x, y, direct):
    px, py = x, y
    result = [(x,y)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        nx, ny = px + dx[direct], py + dy[direct]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if board[nx][ny] == 6:
            break
        result.append((nx, ny))
        px, py = nx, ny
    return set(result)


def two(x, y, direct):
    px, py = x, y
    result = [(x,y)]

    # x고정, y만 바뀜
    if direct == 0:
        while True:
            ny = py + 1
            if ny < 0 or ny >= m:
                break
            if board[x][ny] == 6:
                break
            result.append((x, ny))
            py = ny
        py = y
        while True:
            ny = py - 1
            if ny < 0 or ny >= m:
                break
            if board[x][ny] == 6:
                break
            result.append((x, ny))
            py = ny
    else:
        # y고정, x만 바뀜
        while True:
            nx = px + 1
            if nx < 0 or nx >= n:
                break
            if board[nx][y] == 6:
                break
            result.append((nx, y))
            px = nx
        px = x
        while True:
            nx = px - 1
            if nx < 0 or nx >= n:
                break
            if board[nx][y] == 6:
                break
            result.append((nx, y))
            px = nx
    return set(result)


def three(x, y, direct):
    px, py = x, y
    result = [(x, y)]

    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    # x,y 따로 돌음
    # 그래야 대각선으로 안가고 일직선으로 갈테니
    while True:
        nx = px + dx[direct]
        if nx < 0 or nx >= n:
            break
        if board[nx][y] == 6:
            break
        result.append((nx, y))
        px = nx

    px, py = x, y
    while True:
        ny = py + dy[direct]
        if ny < 0 or ny >= m:
            break
        if board[x][ny] == 6:
            break
        result.append((x, ny))
        py = ny

    return set(result)


def four(x, y, direct):
    px, py = x, y
    result = [(x,y)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    fixing = ['x','y','x','y']

    while True:
        nx, ny = px + dx[direct], py + dy[direct]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if board[nx][ny] == 6:
            break
        result.append((nx, ny))
        px, py = nx, ny

    px, py = x, y
    # x고정, y만 바뀜
    if fixing[direct] == 'x':
        while True:
            ny = py + 1
            if ny < 0 or ny >= m:
                break
            if board[x][ny] == 6:
                break
            result.append((x, ny))
            py = ny
        py = y
        while True:
            ny = py - 1
            if ny < 0 or ny >= m:
                break
            if board[x][ny] == 6:
                break
            result.append((x, ny))
            py = ny
    else:
        # y고정, x만 바뀜
        while True:
            nx = px + 1
            if nx < 0 or nx >= n:
                break
            if board[nx][y] == 6:
                break
            result.append((nx, y))
            px = nx
        px = x
        while True:
            nx = px - 1
            if nx < 0 or nx >= n:
                break
            if board[nx][y] == 6:
                break
            result.append((nx, y))
            px = nx
    return set(result)


def five(x, y):
    px, py = x, y
    result = [(x, y)]

    while True:
        nx = px + 1
        if nx < 0 or nx >= n:
            break
        if board[nx][y] == 6:
            break
        result.append((nx, y))
        px = nx
    px, py = x, y
    while True:
        nx = px - 1
        if nx < 0 or nx >= n:
            break
        if board[nx][y] == 6:
            break
        result.append((nx, y))
        px = nx

    px, py = x, y
    while True:
        ny = py + 1
        if ny < 0 or ny >= m:
            break
        if board[x][ny] == 6:
            break
        result.append((x, ny))
        py = ny
    px, py = x, y
    while True:
        ny = py - 1
        if ny < 0 or ny >= m:
            break
        if board[x][ny] == 6:
            break
        result.append((x, ny))
        py = ny
    return set(result)


def count_unsupervised(supervised):
    # 사각지대 수 = n*m - 감시되는 곳 - wall
    return n*m - len(supervised) - len(wall)


def dfs(depth, visited):
    global answer
    if depth == len(cctv):
        answer = min(answer, count_unsupervised(visited))
        return

    x, y = cctv[depth]
    # 5번 cctv는 회전이 필요없음
    if board[x][y] == 5:
        tmp = five(x, y)
        dfs(depth + 1, visited.union(tmp))

    # 2번은 방향이 2개
    elif board[x][y] == 2:
        for i in range(2):
            tmp = two(x, y, i)
            dfs(depth + 1, visited.union(tmp))
    else:
        # 아니면 4방향 회전하며 감시 지대를 dfs로 탐색
        for i in range(4):
            if board[x][y] == 1:
                # 현재위치, 방향
                # 안에 비추는 곳을 계산하는거를 모듈화 할까 했는데 생각보다 너무 다양스버리
                tmp = one(x, y, i)
            elif board[x][y] == 3:
                tmp = three(x, y, i)
            elif board[x][y] == 4:
                tmp = four(x, y, i)
            dfs(depth + 1, visited.union(tmp))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wall = []
cctv = []


for a in range(n):
    for b in range(m):
        cur = board[a][b]
        if cur != 0:
            if cur == 6:
                wall.append((a, b))
            else:
                cctv.append((a, b))


answer = 100
dfs(0, set())
print(answer)