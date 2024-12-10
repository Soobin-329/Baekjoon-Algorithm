# LCS2
# 골드 4

import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

dp = [ [""] * (len(word2) + 1) for _ in range(len(word1) + 1)]

answer = []

for a in range(1, len(word1) + 1):
    for b in range(1, len(word2) + 1):
        if word1[a-1] == word2[b-1]:
            dp[a][b] = dp[a-1][b-1] + word1[a-1]
        else:
            if len(dp[a][b-1]) >= len(dp[a-1][b]):
                dp[a][b] = dp[a][b-1]
            else:
                dp[a][b] = dp[a-1][b]

# 결과 출력
print(len(dp[-1][-1]))
print(dp[-1][-1])
