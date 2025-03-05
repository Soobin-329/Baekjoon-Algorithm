# 청소년 상어
# 골드 2


import copy
import sys
input = sys.stdin.readline


board = [[] for _ in range(4)]
# 1~17에 물고기 좌표 저장
where_all_fishes = [(99,99)] * 17
for a in range(4):
    one_line = list(map(int, input().split()))
    for b in range(0, 8, 2):
        board[a].append((one_line[b], one_line[b+1]))
        where_all_fishes[one_line[b]] = (a, b//2)


dx = [99, -1,-1,0,1,1,1,0,-1]
dy = [99, 0,-1,-1,-1,0,1,1,1]


answer = -1

# 문제 2: fish_list와 graph를 공유함. 다른 재귀함수에서..


def fish_move(where_the_shark, graph, fish_list, eaten_list):
    for f in range(1, 17):
        if f not in eaten_list:
            x, y = fish_list[f]
            direct = graph[x][y][1]

            if graph[x][y][0] != f:
                print("graph와 fish_list 불일치 >", graph[x][y][0], f, (x,y), fish_list[f])

            # 문제 1: 이미 다음으로 이동했는데도 계속 반복문을 돌면서 회전을 하고 이동을 함
            for i in range(8):
                next_dir = direct + i
                if next_dir > 8:
                    next_dir -= 8

                nx, ny = x+dx[next_dir], y + dy[next_dir]
                # TODO: 회전할때마다 방향을 저장하면 시간초과 나지않을까...?
                graph[x][y] = (graph[x][y][0], next_dir)

                # 움직일 수 없으면 회전
                if 0 > nx or nx > 3 or 0 > ny or ny > 3:
                    continue
                if (nx, ny) == where_the_shark:
                    continue

                # 갈 곳에 물고기 있으면 위치 교환
                # 어쨌든 그래프를 지우진 않으니까 위치교환이겠네
                next_fish = graph[nx][ny][0]
                tmp = fish_list[next_fish]
                fish_list[next_fish] = fish_list[f]
                fish_list[f] = tmp

                tmp = graph[nx][ny]
                graph[nx][ny] = graph[x][y]
                graph[x][y] = tmp

                break

    return graph, fish_list


def dinner_time(shark_size, shark_direct, shark_position, graph, fish_list, eaten_list):
    global answer
    graph, fish_list = fish_move(shark_position, graph, fish_list, eaten_list)

    x, y = shark_position
    for i in range(1, 4):
        nx, ny = x+dx[shark_direct]*i, y+dy[shark_direct]*i
        if 0 > nx or nx > 3 or 0 > ny or ny > 3:
            continue
        # 먹을게 있는지 확인
        if graph[nx][ny][0] not in eaten_list:
            dinner_time(shark_size + graph[nx][ny][0], graph[nx][ny][1], (nx, ny), copy.deepcopy(graph), copy.deepcopy(fish_list), eaten_list + [graph[nx][ny][0]])

    answer = max(answer, shark_size)



dinner_time(board[0][0][0], board[0][0][1], (0, 0), copy.deepcopy(board), copy.deepcopy(where_all_fishes), [board[0][0][0]])

print(answer)