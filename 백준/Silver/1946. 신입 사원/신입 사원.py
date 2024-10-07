# 신입사원
# 실버 1

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    max_a = 0
    max_b = 0

    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
        if a == 1:
            max_b = b
        if b == 1:
            max_a = a

    arr.sort()
    answer = [0]
    higher = arr[0][1]

    # 내 위에 있는 사람중에서 나보다 면접점수가 높은 사람이 있는지만 확인. 있으면 hired 안되고
    for i in range(1, n):
        a, b = arr[i]
        # 전에 있는 사람은 서류 점수가 나보다 높은 사람들이니까
        # 아래 있는 사람은 면접 점수가 높아야 붙는거니까
        # 면접 점수가 위에 있는 사람보다 높은지 비교.
        # 더 높다면, higher 갱신
        if higher > arr[i][1]:
            higher = arr[i][1]
            answer.append(i)

    print(len(answer))