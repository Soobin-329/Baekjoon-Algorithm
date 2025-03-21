# 주유소
# 실버 3


import sys
import copy
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
liter_price = list(map(int, input().split()))

dp = copy.deepcopy(liter_price)

# 제일 마지막(상관없음, 이 가격으로 기름을 살 일이 없음)이랑 제일 첫(어차피 이 가격으로 기름 사서 다음 도시까지 가야함)은 무시
for i in range(n-2, 0, -1):
    dp[i] = min(dp[i], liter_price[i-1])

answer = 0
for i in range(n-1):
    answer += dist[i] * dp[i]

print(answer)