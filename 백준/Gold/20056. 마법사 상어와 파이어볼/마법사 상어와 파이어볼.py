# 마법사 상어와 파이어볼
# 골드 4

import sys
input = sys.stdin.readline

# TODO: 행열은 1에서 시작
# 구하는 것: 남아있는 파이어볼 질량의 합

# r  c  m   d   s
# 행 열 질량 방향 속력

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

"""
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
- 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
- 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
-. 파이어볼은 4개의 파이어볼로 나누어진다. -> 합쳐진게 나누어진다는 말이지?
-  나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
- 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
- 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
- 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
- 질량이 0인 파이어볼은 소멸되어 없어진다.
"""


def move_in_general(x, y, s, d):
    global N, dx, dy

    nx = x + s % N * dx[d]
    ny = y + s % N * dy[d]

    if nx < 0:
        nx += N
    if nx >= N:
        nx -= N
    if ny < 0:
        ny += N
    if ny >= N:
        ny -= N

    return nx, ny


# 파이어볼 이동
def move_fireballs():
    global fireballs

    for i in range(len(fireballs)):
        r, c, m, s, d = fireballs[i]
        nr, nc = move_in_general(r, c, s, d)
        fireballs[i] = [nr, nc, m, s, d]


def distribute_fireballs():
    global fireballs

    new_arr = []
    visited = [False] * len(fireballs)

    fireballs.sort(key=lambda x : (x[0], x[1]))

    for i in range(len(fireballs)):
        if visited[i]:
            continue
        ri, ci, _, _, _ = fireballs[i]
        same_position = [i]
        visited[i] = True

        # 같은 위치에 있는 파이어볼 찾기
        for j in range(i+1, len(fireballs)):
            if visited[j]:
                continue

            rj, cj, _, _, _ = fireballs[j]
            if (ri, ci) == (rj, cj):
                visited[j] = True
                same_position.append(j)
            else:
                break

        if len(same_position) == 1:
            new_arr.append(fireballs[i])

        elif len(same_position) > 1:
            is_all_odd = True
            is_all_even = True
            sum_of_mass = 0
            sum_of_speed = 0

            # 합치기
            for idx in same_position:
                _, _, m, s, d = fireballs[idx]
                sum_of_mass += m
                sum_of_speed += s

                # 방향이 모두 홀수인지 짝수인지 확인
                if d % 2 == 0:
                    is_all_odd = False
                else:
                    is_all_even = False

            # 나누기
            divided_mass = sum_of_mass // 5
            # 질량이 0인 파이어볼은 새로운 리스트에 담지 않는다 (소멸)
            if divided_mass == 0:
                continue

            divided_speed = sum_of_speed // len(same_position)
            divided_directions = [1, 3, 5, 7]

            if is_all_even or is_all_odd:
                divided_directions = [0, 2, 4, 6]

            for new in range(4):
                new_arr.append([ri, ci, divided_mass, divided_speed, divided_directions[new]])

    return new_arr


# 남은 파이어볼 질량 더하기
def sum_final_mass():
    global fireballs
    answer = 0

    for _, _, m, _, _ in fireballs:
        answer += m

    return answer


N, M, K = map(int, input().split())

fireballs = []

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for turn in range(K):
    if len(fireballs) == 0:
        break

    # 파이어볼 이동
    move_fireballs()
    
    # 같은 칸에 있는 파이어볼 모으고 나누기
    fireballs = distribute_fireballs()


# 남은 파이어볼 질량 합치기
print(sum_final_mass())