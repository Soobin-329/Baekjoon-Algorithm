# 숨바꼭질 2
# 골드 4


from collections import deque
n, m = map(int, input().split())

MAX = 10 ** 6
visited = [0] * (MAX + 1)
way = [1] * (MAX + 1)


queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()

    if cur == m:
        break

    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next <= MAX:
            # 같으면 way를 추가
            if visited[next] == visited[cur] + 1:
                way[next] += 1
                queue.append(next)
            elif not visited[next]:
                visited[next] = visited[cur] + 1
                way[next] = 1
                queue.append(next)


print(visited[m])
print(way[m])