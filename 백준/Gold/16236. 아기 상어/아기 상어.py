# 아기 상어
# 골드 3


from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

sx, sy = -1, -1
sharksize = 2
eaten_count = 0
answer = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 상어 위치 찾기
for row, line in enumerate(graph):
    for col, tsize in enumerate(line):
        if tsize == 9:
            sx, sy = row, col
            graph[row][col] = 0
            break


def find_fish(a, b):
    # bfs로 탐색하면서 먹을 수 있는 물고기 배열을 반환하는 함수
    # 최단거리도 같이 반환하므로 가장 짧은 애를 먹으면 되는 것!
    global sharksize
    queue = deque()
    queue.append((a, b))

    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    toeat = []
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= sharksize and not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

                    if graph[nx][ny] < sharksize and graph[nx][ny] != 0:
                        toeat.append((nx, ny, distance[nx][ny]))

    return sorted(toeat, key = lambda x : (x[2],x[0],x[1]))


while True:
    edible = find_fish(sx, sy)

    # 먹을 수 없는 물고기가 없다면
    if len(edible) == 0:
        break       # 엄마 소환

    # 최단거리의 물고기를 먹는다
    sx, sy, time = edible[0]

    answer += time
    graph[sx][sy] = 0
    eaten_count += 1
    if eaten_count == sharksize:
        sharksize += 1
        eaten_count = 0

print(answer)