# LCS
# 골드5

s1 = input().strip()
s2 = input().strip()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)] # 열 행

# 첫 행, 열 세팅 -> 없어도됨???? ㅇㅇㅇ 제일 처음 '' 공백은 같은게 없는거라고 치고 0이라고 하면 맞지 ㅇㅇ

for r in range(1, len(s2)+1):
    for c in range(1, len(s1)+1):
        if s1[c-1] == s2[r-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r][c-1], dp[r-1][c])


print(dp[len(s2)][len(s1)])
