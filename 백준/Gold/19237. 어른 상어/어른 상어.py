# 어른 상어
# 골드 2

import copy

import sys
input = sys.stdin.readline

# 0, 위, 아래, 왼쪽, 오른쪽
dx = [99, -1, 1, 0, 0]
dy = [99, 0, 0, -1, 1]

n, m, k = map(int, input().split())

smell_map = []
lasting_map = [[0] * n for _ in range(n)]
direct_map = [[[99,99,99,99]] for _ in range(m+1)] # 첫 인덱스는 버림(row는 상어, col은 방향)
sharks = [(99,99,99) for _ in range(m+1)] # (x, y, 방향) / 첫 인덱스 버림
alive_sharks = [i for i in range(1, m+1)]

# 입력
for _ in range(n):
    smell_map.append(list(map(int, input().split())))

input_directions = list(map(int, input().split()))

for row in range(n):
    for col, i in enumerate(smell_map[row]):
        if i != 0:
            sharks[i] = (row, col, input_directions[i-1])
            lasting_map[row][col] = k

for i in range(1, m+1):
    for _ in range(4):
        direct_map[i].append(list(map(int, input().split())))




def smell_disappear():
    # 냄새 지속시간 1 감소
    for x in range(n):
        for y in range(n):
            if lasting_map[x][y] != 0:
                if lasting_map[x][y] == 1:
                    smell_map[x][y] = 0
                lasting_map[x][y] -= 1


def shark_move():
    # 상어의 이동방향 결정
    # 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
    # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
    # 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
    for alive in alive_sharks:
        x, y, direct = sharks[alive]
        isMoved = False

        for next_direct in direct_map[alive][direct]:
            nx = x + dx[next_direct]
            ny = y + dy[next_direct]

            if 0 <= nx < n and 0 <= ny < n:
                if smell_map[nx][ny] == 0:
                    sharks[alive] = (nx, ny, next_direct)
                    isMoved = True
                    break

        # 아무 냄새가 없는 칸이 없다면 자신의 냄새가 있는 칸의 방향으로 잡는다
        ## 아 찾았다; 이것도 그냥 막 방향정하는게 아니라 우선순위에 맞춰서 해야겠다
        if not isMoved:
            for next_direct in direct_map[alive][direct]:
                nx = x + dx[next_direct]
                ny = y + dy[next_direct]
                if 0 <= nx < n and 0 <= ny < n:
                    if smell_map[nx][ny] == alive:
                        sharks[alive] = (nx, ny, next_direct)
                        break


def remove_overlap():
    # 겹치는 상어 제거
    # 숫자가 작은게 살아남음
    # 여러개가 겹치면 하나 빼고 다 쫒아냄
    tmp_alive_sharks = copy.deepcopy(alive_sharks)
    for i in range(len(tmp_alive_sharks) - 1, 0, -1):
        alive = tmp_alive_sharks[i]
        x, y, _ = sharks[alive]
        for j in range(i):
            stronger = tmp_alive_sharks[j]
            sx, sy, _ = sharks[stronger]

            if (sx, sy) == (x, y):
                del alive_sharks[i]
                break


def show_dominance():
    # 냄새 뿌리기
    for alive in alive_sharks:
        x, y, direct = sharks[alive]
        smell_map[x][y] = alive
        lasting_map[x][y] = k


def 그림그려줘(flag):
    if flag:
        print("smell map")
        for s in smell_map:
            print(s)
        print()

        print("lasting_map")
        for l in lasting_map:
            print(l)
        print()
    else:
        print(f"alive sharks > {alive_sharks}")
        print(f"sharks > {sharks}")
        상어좌표그리기()
        print()


def 상어좌표그리기():
    tmp_map = [[0] * n for _ in range(n)]

    for a in alive_sharks:
        x, y, direct = sharks[a]
        tmp_map[x][y] = a

    for t in tmp_map:
        print(t)



time = 0
while True:
    time += 1

    # 상어 이동
    shark_move()

    # 겹치는 상어 제거
    remove_overlap()

    # 냄새 지속시간 1 감소
    smell_disappear()

    # 냄새 뿌리기
    show_dominance()

    # 1번 상어만 남았는지 확인
    if len(alive_sharks) == 1:
        break
    if time >= 1000:
        time = -1
        break


print(time)