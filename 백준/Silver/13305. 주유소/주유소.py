# 주유소
# 실버 3


import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
fuel = list(map(int, input().split()))
cost = 0
cur = fuel[0]

for i in range(n-1):
    cost += cur * dist[i]
    if fuel[i+1] < cur:
        cur = fuel[i+1]

print(cost)