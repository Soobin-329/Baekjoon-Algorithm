# 시험 감독
# 브론즈 2
# 15:40 ~ 16:07

import math
import sys

input = sys.stdin.readline


n = int(input())
arr = map(int, input().split())
b, c = map(int, input().split())

sum = 0

for a in arr:
    if (a-b) > 0:
        sum += int(math.ceil((a - b) / c)) + 1
    else:
        sum += 1

print(sum)