# 기타리스트
# 실버 1


import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp=[[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1 # 0번째에는 5볼륨으로 플레이 된다는 것

for i in range(1, n+1):
    for j in range(m + 1):
        if dp[i-1][j] > 0: # 전번에 j볼륨으로 플레이 되었다면,
            # 더했을 때 범위에 맞다면 저장
            if 0 <= j + v[i-1] <= m:
                dp[i][j + v[i-1]] = 1
            # 뺐을 때 범위에 맞다면 저장
            if 0 <= j - v[i-1] < m:
                dp[i][j - v[i-1]] = 1

answer = -1
for i in range(m, -1, -1):
    # 마지막 번째 플레이 음량 배열을 돌면서 플레이 된 음량 중 가장 큰거 찾기
    if dp[n][i] == 1:
        answer = i
        break

print(answer)