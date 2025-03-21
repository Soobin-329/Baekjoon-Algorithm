# 부분합
# 골드 4


import sys
input = sys.stdin.readline

MAX = 100001

n, s = map(int, input().split())
arr = list(map(int, input().split()))

front, back = 0, 0
shortest = MAX
hap = arr[0]

while front <= back <= n:
    if hap >= s:
        # 앞 포인터 옮기기
        hap -= arr[front]
        front += 1

        shortest = min(shortest, back - front + 2)
    else:
        back += 1
        if back < n:
            hap += arr[back]


if shortest == MAX:
    print(0)
else:
    print(shortest)