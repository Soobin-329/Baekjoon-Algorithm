# 숨바꼭질
# 실버 1
# 꼭 다시 풀어보기~

from collections import deque
n, k = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)


def bfs(s):
    queue = deque()
    queue.append(s)

    while queue:
        cur = queue.popleft()
        if cur == k:
            return visited[k]
        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[cur] + 1
                queue.append(i)
                

print(bfs(n))