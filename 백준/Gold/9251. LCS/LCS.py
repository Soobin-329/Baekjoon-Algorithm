# LCS
# 골드5

s1 = input().strip()
s2 = input().strip()

dp = [[0] * (len(s2)+1) for _ in range(len(s1) + 1)]

for a in range(1, len(s1) + 1):
    for b in range(1, len(s2) + 1):
        if s1[a - 1] == s2[b - 1]:
            dp[a][b] = dp[a-1][b-1] + 1

        else:
            dp[a][b] = max(dp[a-1][b], dp[a][b-1])

print(dp[-1][-1])
