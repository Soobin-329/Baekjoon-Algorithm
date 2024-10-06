# ATM
# 실버 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum = 0
time = 0
for a in arr:
    time += a
    sum += time

print(sum)