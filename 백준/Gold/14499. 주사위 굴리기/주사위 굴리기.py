# 주사위 굴리기
# 골드 4


import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

# 아랫면은 6, 윗면은 1
dice = [0,0,0,0,0,0]
dx = [999, 0,0,-1,1]
dy = [999, 1,-1,0,0]


# 동쪽(0,1)은 1, 서쪽(0,-1)은 2, 북쪽(-1,0)은 3, 남쪽(1,0)은 4
def roll(direction):
    global dice
    one, two, three, four, five, six = map(int, dice)
    # 동, 오른쪽
    if direction == 1:
        dice = [four,two,one,six,five,three]
    # 서, 왼쪽
    if direction == 2:
        dice = [three,two,six,one,five,four]
    # 북, 앞
    if direction == 3:
        dice = [five,one,three,four,six,two]
    # 남, 뒤
    if direction == 4:
        dice = [two,six,three,four,one,five]



for d in directions:
    nx = x + dx[d]
    ny = y + dy[d]

    # board의 범위를 벗어나면 출력하지도, 움직이지도 않음
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 주사위 굴리기
    roll(d)

    # 밑면 복사
    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    # 보드 값이 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
    # 칸에 쓰여 있는 수는 0이 된다
    if board[nx][ny] != 0:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = dice[5]
        
    # 윗면 출력
    print(dice[0])

    # x,y 재설정
    x, y = nx, ny

