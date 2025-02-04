# 일곱 난쟁이
# 브론즈 1

import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
    heights.append(int(input()))
imposters = []

sum_heights = sum(heights)
flag = True
for a in range(9):
    if flag:
        for b in range(a+1, 9):
            # 7명의 키를 더하면 100
            if sum_heights - (heights[a] + heights[b]) == 100:
                imposters.append(a)
                imposters.append(b)
                flag = False
                break

# 결과 출력
dwarfs = []
for i in range(9):
    if i not in imposters:
        dwarfs.append(heights[i])

dwarfs.sort()

for d in dwarfs:
    print(d)