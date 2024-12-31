# 나만 안되는 연애
# 골드 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gender = input().strip().split()

graph = []
for _ in range(m):
    u, v, d = map(int, input().split())
    graph.append((u, v, d))

graph.sort(key=lambda x:x[2])

parents = [x for x in range(n+1)]


def find_parent(x):
    if x == parents[x]:
        return x
    return find_parent(parents[x])


def same_parent(x, y):
    return find_parent(x) == find_parent(y)


def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px < py:
        parents[px] = py
    else:
        parents[py] = px


# 모든 학교가 연결되어있는지 확인
def isConnected():
    root = max(parents)

    for a in range(1, n+1):
        if find_parent(a) != root:
            return False
    return True


answer = 0

for a, b, c in graph:
    if not same_parent(a, b):
        # 같은 성별의 대학이라면 continue
        if gender[a-1] == gender[b-1]:
            continue
        union_parent(a, b)
        answer += c

if isConnected():
    print(answer)
else:
    print("-1")