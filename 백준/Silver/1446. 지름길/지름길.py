# 고속도로
# 실버 1

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
graph = [i for i in range(d+1)]
ways = []

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    if b - a <= c:
        continue
    ways.append([a, b, c])

ways.sort()

for i in range(len(ways)):
    start, end, weight = ways[i]

    for a in range(1, d+1):
        if a == end:
            graph[a] = min(graph[a], graph[start] + weight)
        else:
            graph[a] = min(graph[a], graph[a - 1]+1)

print(graph[d])
