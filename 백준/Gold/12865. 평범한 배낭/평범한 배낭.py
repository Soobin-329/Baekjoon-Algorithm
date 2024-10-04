# 평범한 배낭
# 골드 5

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [[0 for _ in range(k+1)] for _ in range(n+1)]
stuff = [[0,0]]

for i in range(n):
    w, v = map(int, input().split())
    stuff.append([w, v])

# i: 배낭에 들어있는 물건 수
for i in range(1, n+1):
    # j: 배낭의 무게
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j >= weight:
            d[i][j] = max(d[i-1][j], value + d[i-1][j-weight])
        else:
            d[i][j] = d[i-1][j]

print(d[n][k])
