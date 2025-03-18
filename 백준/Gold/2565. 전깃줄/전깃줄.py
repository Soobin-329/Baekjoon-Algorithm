# 전깃줄
# 골드 5


import sys
input = sys.stdin.readline

n = int(input())
arr = []

dp = [1] * n

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x:x[0])


for i in range(1, n):
    for j in range(i):
        a, b = arr[i]
        if b > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))