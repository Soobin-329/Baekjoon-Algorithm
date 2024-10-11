# 상어 초등학교
# 골드 5


n = int(input())
students = [[] for _ in range(n**2+1)]

from collections import deque
queue = deque()
graph = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def find_many_like_cells(student, likes):
    global graph
    answer = []
    max_count = -1

    for a in range(n):
        for b in range(n):
            count = 0

            # 그 칸이 비어있는지 않으면, 이미 차지된 칸이므로 대상에서 제외
            if graph[a][b] != 0:
                continue

            for i in range(4):
                nx = a+dx[i]
                ny = b+dy[i]

                # 범위에 맞는지 확인
                if 0 <= nx < n and 0 <= ny < n:
                    # 좋아하는 학생이 인접하다면, count++
                    if graph[nx][ny] in likes:
                        count += 1
                        continue
            # count가 answer에 있는 것과 같으면 append
            if count >= 1:
                if count == max_count:
                    answer.append((a,b))

                # count가 answer에 있는 것보다 크다면 answer 초기화, append
                elif count > max_count:
                    max_count = count
                    answer = [(a,b)]
    return answer


def find_many_empty_cells(cells):
    # cells의 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    answer = []
    max_count = -1  # 비어있는 칸 세기

    for cell in cells:
        a, b = cell
        count = 0

        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            # 범위에 맞는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 비어있는 칸이 인접하다면, count++
                if graph[nx][ny] == 0:
                    count += 1
                    continue
        # count가 answer에 있는 것과 같으면 append
        if count >= 1:
            if count == max_count:
                answer.append((a,b))

            # count가 answer에 있는 것보다 크다면 answer 초기화, append
            elif count > max_count:
                max_count = count
                answer = [(a,b)]
    return answer


for i in range(n**2):
    likes = list(map(int, input().split()))
    students[likes[0]] = likes[1:]
    queue.append((likes[0], likes[1:]))


while queue:
    student, likes = queue.popleft()

    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    like_cells = find_many_like_cells(student, likes)

    if len(like_cells) == 1:
        x, y = like_cells[0]
        graph[x][y] = student

    else:
        # 좋아하는 학생이 인접한 칸이 없다면, 빈 모든 칸을 대상으로 다시 탐색하도록
        if len(like_cells) == 0:
            for a in range(n):
                for b in range(n):
                    if graph[a][b] == 0:
                        like_cells.append((a,b))

        # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        empty_cells = find_many_empty_cells(like_cells)

        if len(empty_cells) == 1:
            x, y = empty_cells[0]
            graph[x][y] = student

        else:
            if len(empty_cells) == 0:
                # 주변에 비어있는 칸의 우선순위를 정할 수 없다면, like_cells를 대상으로 다시 탐색
                empty_cells = like_cells

            # 3 .2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
            empty_cells.sort(key = lambda x : (x[0], x[1]))
            x, y = empty_cells[0]
            graph[x][y] = student


# 만족도 구하기
sum = 0

for a in range(n):
    for b in range(n):
        count = 0
        likes = students[graph[a][b]]

        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            # 범위에 맞는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 좋아하는 학생이 인접하다면, count++
                if graph[nx][ny] in likes:
                    count += 1
                    continue

        if count == 1:
            sum += 1
        elif count == 2:
            sum += 10
        elif count == 3:
            sum += 100
        elif count == 4:
            sum += 1000

print(sum)