# 유기농 배추
# 실버 2


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방문한곳은 graph를 False로 만들어주면 될 것 같다.
def dfs(x, y):
    global graph
    if not graph[x][y]:
        return
    graph[x][y] = False

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            dfs(nx, ny)


dx = [0,0,-1,1]
dy = [1,-1,0,0]

testcases = int(input())
for _ in range(testcases):
    m, n, k = map(int, input().split())
    graph = [[False] * n for _ in range(m)]
    cabbages = []
    answer = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = True
        cabbages.append((x, y))

    for c in cabbages:
        x, y = c[0], c[1]
        if graph[x][y]:
            dfs(x, y)
            answer += 1

    print(answer)