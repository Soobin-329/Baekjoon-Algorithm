# 스티커
# 실버 1

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    d = [[0 for _ in range(n)] for _ in range(2)]

    for _ in range(2):
        arr.append(list(map(int, input().split())))

    # n이 1일 때:
    if n == 1:
        d[0][0] = arr[0][0]
        d[1][0] = arr[1][0]

    else:
        d[0][0] = arr[0][0]
        d[1][0] = arr[1][0]
        d[0][1] = arr[0][1] + arr[1][0]
        d[1][1] = arr[1][1] + arr[0][0]

        for col in range(2, n):
            for row in range(2):
                if row == 1:
                    nrow = 0
                else:
                    nrow = 1
                if d[row][col-1] - arr[row][col-1] > d[nrow][col-1]:
                    d[row][col] = arr[row][col] + d[nrow][col-2]
                else:
                    d[row][col] = arr[row][col] + d[nrow][col-1]

    print(max(d[0][n-1], d[1][n-1]))