import sys
sys.setrecursionlimit(10**7)

def dfs(count, health, dungeons, visited):
    global answer
    
    for i in range(len(dungeons)):
        if not visited[i]:
            if health >= dungeons[i][0]:
                visited[i] = True
                dfs(count + 1, health - dungeons[i][1], dungeons, visited)
                visited[i] = False
    
    answer = max(count, answer)

def solution(k, dungeons):
    global answer
    
    visited = [ False for _ in range(len(dungeons))]
    
    answer = -1
    dfs(0, k, dungeons, visited)

    return answer
