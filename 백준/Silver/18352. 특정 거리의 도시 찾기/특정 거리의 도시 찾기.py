# 특정 거리의 도시 찾기
# 실버 2

import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

INF = 999999
graph =  [[] for _ in range(n+1)]
answer = []
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


# 다익스트라
import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist,now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        # 연결된 모든 노드 탐색
        for next, nextDist in graph[now]:
            if dist + nextDist < distance[next]:
                distance[next] = dist + nextDist
                heapq.heappush(queue, (dist+nextDist, next))

dijkstra(x)

for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a)