# AC
# 골드 5

import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    result = ''
    error_flag = False

    # 입력
    func = input()
    n = int(input())
    arr = input().strip()[1:-1].split(',')
    queue = deque(arr)

    if n == 0:
        queue = []

    r_count = 0
    for i, f in enumerate(func):
        if f == 'R':
            r_count += 1
        elif f == 'D':
            # 배열이 비어있을 때, 에러가 발생
            if len(queue) < 1:
                error_flag = True
                break
            else:
                if r_count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if error_flag:
        print("error")
        continue

    # 배열 형태로 만들어주기
    if r_count % 2 == 0:
        print("[" + ",".join(queue) + "]")
    else:
        queue.reverse()
        print("[" + ",".join(queue) + "]")