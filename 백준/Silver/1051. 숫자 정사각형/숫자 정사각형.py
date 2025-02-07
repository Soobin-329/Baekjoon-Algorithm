# 숫자 정사각형
# 실버 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(input().strip())


for length_of_side in range(min(n, m) - 1, 0, -1):
    # 정사각형의 left top 좌표로 반복문
    for a in range(n - length_of_side):
        for b in range(m - length_of_side):
            if maps[a][b] == maps[a][b+length_of_side] == maps[a+length_of_side][b] == maps[a+length_of_side][b+length_of_side]:
                print((length_of_side + 1) ** 2)
                exit()

# 탐색이 끝난 후에도 정답 정사각형이 없다면 1 출력
print(1)
