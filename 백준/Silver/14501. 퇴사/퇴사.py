# 퇴사
# 실버 3
# 재귀적 풀이

import sys
input = sys.stdin.readline

n = int(input())
plan = [(0,0)]

for _ in range(n):
    t, p = map(int, input().split())
    plan.append((t,p))


def work(day, money):
    global answer
    if day > n:
        answer = max(answer, money)
        return

    time, value = plan[day]

    if day + time <= (n + 1):
        # 그 날의 일을 받는 것과 안 받는 것 둘 다
        work(day + time, money + value)
        work(day + 1, money)
    else:
        # 퇴사일 이후의 일이라면 그 다음날로 이동
        work(day + 1, money)


answer = 0
for i in range(1, n + 1):
    work(i, 0)

print(answer)