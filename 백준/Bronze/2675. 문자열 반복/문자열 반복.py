# 문자열 반복
# 브론즈 2

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    inputs = input().strip().split()
    n, s = int(inputs[0]), inputs[1]

    for c in s:
        for _ in range(n):
            print(c, end='')
    print()