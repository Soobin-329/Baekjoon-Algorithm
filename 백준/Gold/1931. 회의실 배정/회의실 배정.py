# 회의실 배정
# 골드 5


import sys
input = sys.stdin.readline

n = int(input())

arr = []


for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x:(x[1], x[0]))

# 첫 회의는 무조건 선택
count = 1
prev_end = arr[0][1]

for i in range(1, len(arr)):
    start, end = arr[i]

    if start >= prev_end:
        count += 1
        prev_end = end


print(count)