# 퇴사
# 실버 3
# DP - Bottom up 방식

import sys
input = sys.stdin.readline

n = int(input())
plan = []

for i in range(n):
    plan.append(list(map(int, input().split())))

# DP 사용
# 각 날짜의 최대 수익을 담는 것
dp = [0 for i in range(n + 1)]

for day in range(n):
    # (day + 상담기간) 부터 퇴사일까지 반복문
    for next in range(day + plan[day][0], n + 1):
        # 상담으로 얻을 수 있는 수익이 이때까지 dp에서 갖고있던 수익보다 더 크면 갱신
        # 예를 들어, 1일차에 3일걸리는 10가치의 상담을 진행했을 때,
        # dp는 이렇게 순서대로 바뀔 것임
        # [0,0,0,10,0,0,0,0], [0,0,0,10,10,0,0,0], ... , [0,0,0,10,10,10,10,10]
        if dp[next] < dp[day] + plan[day][1]:
            dp[next] = dp[day] + plan[day][1]

print(dp[-1])