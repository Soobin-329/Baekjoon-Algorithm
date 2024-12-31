# 최소 스패닝 트리
# 골드 4


import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a,b,c))

graph.sort(key=lambda x:x[2])

parents = [i for i in range(v+1)]


def find_parent(a):
    if a == parents[a]:
        return a
    return find_parent(parents[a])


def same_parents(a, b):
    return find_parent(a) == find_parent(b)


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parents[pa] = pb
    else:
        parents[pb] = pa


answer = 0
for a, b, c in graph:
    if not same_parents(a, b):
        union_parent(a, b)
        answer += c

print(answer)