# 톱니바퀴
# 골드 5



import sys
from collections import deque
input = sys.stdin.readline


def calculateFinalScore():
    global wheels
    result = 0

    if wheels[0][0] == 1:
        result += 1
    if wheels[1][0] == 1:
        result += 2
    if wheels[2][0] == 1:
        result += 4
    if wheels[3][0] == 1:
        result += 8

    return result


def isRotating(cur, direct):
    global queue, wheels

    if direct == 1:
        opposite = -1
    else:
        opposite = 1

    if 0 <= cur + 1 < 4 and not visited[cur + 1]:
        # cur의 오른쪽과 next(cur+1)의 왼쪽 비교
        if wheels[cur][2] != wheels[cur+1][6]:
            queue.append((cur+1, opposite))
    if 0 <= cur - 1 < 4 and not visited[cur - 1]:
        # cur의 오른쪽과 next(cur-1)의 왼쪽 비교
        if wheels[cur][6] != wheels[cur-1][2]:
            queue.append((cur-1, opposite))


def rotate(idx, direct):
    global wheels

    one, two, three, four, five, six, seven, eight = wheels[idx]

    # 시계방향 회전
    if direct == 1:
        wheels[idx] = [eight, one, two, three, four, five, six, seven]
    # 반시계방향 회전
    else:
        wheels[idx] = [two, three, four, five, six, seven, eight, one]



wheels = [[] for _ in range(4)]

for i in range(4):
    tmp = input().strip()
    for t in tmp:
        wheels[i].append(int(t))

k = int(input())
for _ in range(k):
    wheelNum, direction = map(int, input().split())
    wheelNum -= 1

    visited = [False] * 4

    queue = deque([(wheelNum, direction)])

    while queue:
        idx, direct = queue.popleft()
        visited[idx] = True

        # 회전하기 전에 맞닿은 곳을 회전할지말지 봐야함
        # 큐에 넣기까지
        isRotating(idx, direct)

        # 회전
        rotate(idx, direct)

print(calculateFinalScore())