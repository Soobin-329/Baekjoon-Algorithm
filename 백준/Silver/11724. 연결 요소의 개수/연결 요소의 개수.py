# 연결요소의 개수
# 실버 2


import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # graph.append(tuple(map(int, input().split())))
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque([i for i in range(1, n+1)])
    components = [i for i in range(n+1)]
    visited = [False for _ in range(n+1)]

    while queue:
        # cur = 1
        cur = queue.popleft()
        visited[cur] = True
        for c in graph[cur]:
            components[c] = components[cur]
            if not visited[c]:
                queue.append(c)

    return components


components = bfs()
count_set = set(components)
print(len(count_set) - 1)