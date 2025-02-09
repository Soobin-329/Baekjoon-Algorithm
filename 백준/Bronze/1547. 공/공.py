# 공
# 브론즈 3

m = int(input())

# 공의 현재 위치
ball = 1
moves = []
for _ in range(m):
    moves.append(list(map(int, input().strip().split())))

for move in moves:
    if ball not in move:
        continue

    # 공의 위치 변환
    if move[0] == ball:
        ball = move[1]
    else:
        ball = move[0]

print(ball)