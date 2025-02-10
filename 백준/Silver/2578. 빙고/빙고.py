# 빙고
# 실버 4

import sys
input = sys.stdin.readline


def howManyBingos(row, col):
    result = 0
    # 가로 빙고 체크
    for a in range(5):
        if not visited[row][a]:
            break
        if a == 4:
            result += 1
    # 세로 빙고 체크
    for b in range(5):
        if not visited[b][col]:
            break
        if b == 4:
            result += 1
    # 대각선 아래 빙고 체크
    if row == col:
        for c in range(5):
            if not visited[c][c]:
                break
            if c == 4:
                result += 1
    # 대각선 위 빙고 체크
    if row + col == 4:
        for d in range(5):
            if not visited[d][4-d]:
                break
            if d == 4:
                result += 1

    return result


visited = [[False] * 5 for _ in range(5)]
board = []
calling = []

for _ in range(5):
    board.append(list(map(int, input().split())))

for _ in range(5):
    calling += list(map(int, input().split()))


bingos = 0
for idx, call in enumerate(calling):
    for a in range(5):
        for b in range(5):
            if board[a][b] == call:
                visited[a][b] = True
                bingos += howManyBingos(a, b)
                break

    if bingos >= 3:
        print(idx + 1)
        break
