# 경사로
# 골드 3


import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


answer = 0
visited = [[False] * n for _ in range(n)]

# 가로 확인
for row in range(n):
    cur_level = graph[row][0]
    flag = True
    for col in range(1, n):
        prev_level = cur_level
        cur_level = graph[row][col]

        if not flag:
            break

        if cur_level == prev_level:
            continue
        elif abs(cur_level-prev_level) > 1:
            flag = False

        # 지금게 더 높으면, 이전 l개의 것이 같은 높이여야함
        elif cur_level > prev_level:
            for i in range(1, l+1):
                if col - i < 0 or prev_level != graph[row][col-i] or visited[row][col-i]:
                    flag = False
                    break
            # 경사면 두기
            if flag:
                for i in range(1, l + 1):
                    visited[row][col - i] = True

        # 지금게 더 낮으면, 이후 l개의 것이 같은 높이여야함
        else:
            for i in range(l):
                if col + i >= n or cur_level != graph[row][col+i] or visited[row][col+i]:
                    flag = False
                    break
            # 경사면 두기
            if flag:
                for i in range(l):
                    visited[row][col + i] = True
    if flag:
        answer += 1


visited = [[False] * n for _ in range(n)]

for col in range(n):
    cur_level = graph[0][col]
    flag = True
    for row in range(1, n):
        prev_level = cur_level
        cur_level = graph[row][col]

        if not flag:
            break

        if cur_level == prev_level:
            continue
        elif abs(cur_level-prev_level) > 1:
            flag = False

        # 지금게 더 높으면, 이전 l개의 것이 같은 높이여야함
        elif cur_level > prev_level:
            for i in range(1, l+1):
                if row - i < 0 or prev_level != graph[row-i][col] or visited[row-i][col]:
                    flag = False
                    break
            # 경사면 두기
            if flag:
                for i in range(1, l + 1):
                    visited[row-i][col] = True
        # 지금게 더 낮으면, 이후 l개의 것이 같은 높이여야함
        else:
            for i in range(l):
                if row + i >= n or cur_level != graph[row+i][col] or visited[row+i][col]:
                    flag = False
                    break

            # 경사면 두기
            if flag:
                for i in range(l):
                    visited[row+i][col] = True
    if flag:
        answer += 1

print(answer)