# 가장 긴 바이토닉 부분 수열
# 골드 4


import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
reverse_a = []

for i in range(n-1, -1, -1):
    reverse_a.append(a[i])

up = [1] * n
down = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            up[i] = max(up[i], up[j] + 1)
        if reverse_a[i] > reverse_a[j]:
            down[i] = max(down[i], down[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, up[i]+down[n-i-1] - 1)

print(answer)