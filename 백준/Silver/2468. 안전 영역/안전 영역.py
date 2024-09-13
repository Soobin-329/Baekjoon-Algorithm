import sys
sys.setrecursionlimit(10000)


def dfs(a, b, rain):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    if graph[a][b] > rain and not visited[a][b]:
        visited[a][b] = True
        for i in range(4):
            if (0 <= a + dx[i] < n) and (0 <= b + dy[i] < n):
                dfs(a + dx[i], b + dy[i], rain)


n = int(sys.stdin.readline())

graph = []
minh, maxh = 101, -1
answer = 1

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)
    maxh = max(max(line), maxh)


for rain in range(1, maxh + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if (graph[i][j] > rain) and not visited[i][j]:
                # 안전영역
                dfs(i, j, rain)
                count += 1

    answer = max(answer, count)

print(answer)
