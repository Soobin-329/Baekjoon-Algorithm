# 괄호
# 실버 4

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    left = 0
    flag = True
    string = input()

    for s in string:
        if s == '(':
            left += 1
        elif s==')':
            if left == 0:
                flag = False
                break
            else:
                left -= 1

    if left != 0:
        flag = False


    if flag:
        print("YES")
    else:
        print("NO")
