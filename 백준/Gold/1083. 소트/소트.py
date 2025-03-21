# 소트
# 골드 4

import sys
input = sys.stdin.readline

n, nums = int(input()), list(map(int, input().split()))
s = int(input())

for i in range(n):
    # i번째에서 가질 수 있는 최대 값을 앞으로 땡겨오는거구나
    # 그럼 i+1로, 다음으로 넘어갈 수 있지..!
    
    # 탐색
    max_num = max(nums[i: min(n, i + s + 1)])
    idx = nums.index(max_num)

    # 교환
    for j in range(idx, i, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
    # 후처리
    s -= (idx - i)

    if s <= 0: break

print(*nums)