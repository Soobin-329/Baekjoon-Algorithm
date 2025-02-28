# 퇴사 2
# 골드 5

MAX = 15000001
dp = [0] * MAX

import sys
input = sys.stdin.readline

schedule = []

n = int(input())
for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

for day in range(len(schedule) - 1, -1, -1):
    t, p = schedule[day]

    # 퇴사일을 넘는 상담은 받지 않음
    if day + t > n:
        dp[day] = dp[day + 1]
        continue

    # 일을 받는게 나을지, 안받는게 하루를 보내는게 나을지
    dp[day] = max(dp[day + t] + p, dp[day + 1])


print(dp[0])