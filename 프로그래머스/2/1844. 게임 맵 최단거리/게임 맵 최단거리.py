from collections import deque
    
def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0:
                    continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 1 + maps[x][y]  
                    queue.append((nx, ny))
               
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    return answer