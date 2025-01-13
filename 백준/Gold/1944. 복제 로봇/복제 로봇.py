# 복제 로봇
# 골드 1

# 포인트
# 1. S와 K의 구분 X
# 2. bfs로 각 노드의 거리 구하기(S와 K를 만나면 더이상 탐색하지 않았는데(어차피 거기서 다시 시작하니까) 근데 거기서 멈추지 않고 더 가야지 정답이 나왔다...)
# 3. 거리 구한거로 크루스칼

# 메모리 초과가 났을때 해결방법
# graph가 좌표 두 개를 갖고있으니까 너무 커진듯. 그거를 keys의 idx를 갖는 식으로 변경. maps에 원래 K와 S가 있는 곳을 keys에 해당하는 idx를 넣어주면 해결되는 일!

import sys
from collections import deque
input = sys.stdin.readline

graph = []
maps = []
keys = []

n, m = map(int, input().split())

for _ in range(n):
    maps.append(list(input().strip()))

# s와 key의 좌표 구하기
for i in range(1, n-1):
    for j in range(1, n-1):
        if maps[i][j] == "S" or maps[i][j] == "K":
            maps[i][j] = len(keys)
            keys.append((i, j))


# bfs로 s-k, k-k 거리 구하기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(m):
    visited = [[False] * n for _ in range(n)]
    sx, sy = keys[i][0], keys[i][1]
    queue = deque([(sx, sy, 0)])

    while queue:
        x, y, dist = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if maps[nx][ny] != "1" and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

                if maps[nx][ny] != '0':
                    graph.append((i, maps[nx][ny], dist+1))


# 크루스칼
answer = 0
count = 0
graph.sort(key=lambda x:x[2])

parents = [x for x in range(m+1)] 


def find_parent(a):
    if a == parents[a]:
        return a
    return find_parent(parents[a])


def same_parent(a, b):
    return find_parent(a) == find_parent(b)


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parents[pa] = pb
    else:
        parents[pb] = pa


for a, b, c in graph:
    if not same_parent(a, b):
        answer += c
        count += 1
        union_parent(a, b)

# 모두 연결되어있는지 확인
if answer == 0 or count != m:
    print(-1)
else:
    print(answer)