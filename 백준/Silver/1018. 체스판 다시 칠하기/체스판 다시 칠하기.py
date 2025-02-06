# 체스판 다시 칠하기
# 실버 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input().strip())

perfect_board = ['BWBWBWBW','WBWBWBWB','BWBWBWBW'
                ,'WBWBWBWB','BWBWBWBW','WBWBWBWB'
                ,'BWBWBWBW','WBWBWBWB']

# 다시 칠해야 하는 정사각형 개수의 최솟값
answer = 100

# 슬라이딩 윈도우
for a in range(n-7):
    for b in range(m-7):
        paint_count = 0
        # 칠해야 할 부분 비교
        for x, line in enumerate(board[a:a+8]):
            for i in range(b, b+8):
                if line[i] != perfect_board[x][i-b]:
                    paint_count += 1

        # W부터 시작하는 보드판이면 대칭이므로
        answer = min(answer, min(paint_count, 64-paint_count))

print(answer)