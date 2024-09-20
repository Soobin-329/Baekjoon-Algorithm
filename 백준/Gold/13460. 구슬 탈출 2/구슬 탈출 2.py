
import sys
from collections import deque


def bfs(rx, ry, bx, by):
    count = 0
    queue = deque()
    queue.append((rx, ry, bx, by))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []
    visited.append((rx, ry, bx, by))

    while queue:
        for _ in range(len(queue)):     
            rx, ry, bx, by = queue.popleft()
            if count > 10:  
                print(-1)
                return
            if graph[rx][ry] == 'O':  
                print(count)
                return

            for i in range(4):
                nrx, nry = rx, ry
                nbx, nby = bx, by

                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    elif graph[nrx][nry] == 'O':
                        break

                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    elif graph[nbx][nby] == 'O':
                        break

                if graph[nbx][nby] == 'O':
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):  
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))

        count += 1
    print(-1)



n, m = map(int, sys.stdin.readline().split())

graph = []

for row in range(n):
    line = sys.stdin.readline()
    graph.append(list(line))
    for col in range(m):
        if graph[row][col] == 'R':
            rx, ry = row, col
        elif graph[row][col] == 'B':
            bx, by = row, col

bfs(rx, ry, bx, by)

