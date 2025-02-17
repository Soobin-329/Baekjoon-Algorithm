from collections import deque
import sys

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [ [] for _ in range(n+1) ]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        # 아직 방문하지 않았다면,
        if not visited[i]:
            # 방문하기
            dfs(i, graph, visited)


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v, graph, visited1)
print()
bfs(v, graph, visited2)