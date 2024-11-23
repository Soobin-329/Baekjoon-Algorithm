# 좋은 친구
# 골드 4


import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(len(input().rstrip()))

queue = [ deque() for _ in range(21) ]
answer = 0

for i, l in enumerate(arr):
    # 좋은 친구가 아님
    while queue[l] and i - queue[l][0] > k:
        queue[l].popleft()
    if queue[l]:
        answer += len(queue[l])

    queue[l].append(i)


print(answer)