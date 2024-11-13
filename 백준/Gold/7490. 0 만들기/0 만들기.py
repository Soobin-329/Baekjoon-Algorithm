# 0 만들기
# 골드5

import sys

input = sys.stdin.readline

global result

def dfs(idx, n, string):
    if idx >= n:
        if eval(string.replace(' ', '')) == 0:
            result.append(string)
        return
    n_idx = idx + 1
    dfs(n_idx, n, string + " " + str(n_idx))
    dfs(n_idx, n, string + "+" + str(n_idx))
    dfs(n_idx, n, string + "-" + str(n_idx))


   
testcase = int(input())

for _ in range(testcase):
    n = int(input())
    result = []

    dfs(1, n, "1")

    for a in result:
        print(a)

    print()