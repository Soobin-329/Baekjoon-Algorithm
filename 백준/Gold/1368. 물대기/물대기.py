# 물대기
# 골드 2

import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append((n, i, int(input())))


costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))


for a in range(n):
    for b in range(a+1, n):
        if a == b:
            continue
        graph.append((a, b, costs[a][b]))

graph.sort(key=lambda x:x[2])

parents = [x for x in range(n+1)]
answer = 0


def find_parents(a):
    if parents[a] == a:
        return a
    return find_parents(parents[a])


def same_parents(a, b):
    return find_parents(a) == find_parents(b)


def union_parent(a, b):
    pa = find_parents(a)
    pb = find_parents(b)

    if pa < pb:
        parents[pa] = pb
    else:
        parents[pb] = pa


for a, b, c in graph:
    if not same_parents(a, b):
        union_parent(a, b)
        answer += c

print(answer)