# 스타트와 링크
# 실버 1


import sys
input = sys.stdin.readline

n = int(input())
graph = []
visited = [ False for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))


def calcPower(players):
    power = 0
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            a, b = players[i], players[j]
            power += graph[a][b] + graph[b][a]

    return power


def getScore():
    # 스타트팀: start, 링크팀: link
    start = []
    link = []

    for i in range(n):
        if visited[i]:
            start.append(i)
        else:
            link.append(i)

    return abs(calcPower(start) - calcPower(link))


def dfs(depth, player):
    global answer
    if depth == n//2:
        answer = min(answer, getScore())
        return

    for i in range(player, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


answer = 99999999999999999
dfs(0, 0)
print(answer)