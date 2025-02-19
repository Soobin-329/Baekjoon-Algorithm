# 단지번호붙이기
# 실버 1


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []

for _ in range(n):
    graph.append(input().strip())

answer = []
visited = [[False] * n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x, y):
    global visited, nh
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == '1' and not visited[nx][ny]:
                nh += 1
                dfs(nx, ny)


for x in range(n):
    for y in range(n):
        if graph[x][y] == '1' and not visited[x][y]:
            nh = 1
            dfs(x, y)
            answer.append(nh)

# 출력
answer.sort()
print(len(answer))
for a in answer:
    print(a)