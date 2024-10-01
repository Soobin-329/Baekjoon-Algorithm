def solution(triangle):
    answer = 0
    
    d = [0] * ((len(triangle) - 1) ** 2)
    
    d[0] = triangle[0][0]
    
    # 내려오면서 이때까지 더한 것의 최대를 기록한다
    # total은 현재 레벨 위에 있는 노드의 수(거쳐온 노드 수)
    total = 0
    for level in range(1, len(triangle)):
        total += level
        prev = len(triangle[level - 1])
        for i, num in enumerate(triangle[level]):
            # 내 부모
            right = i + total - prev
            left = i + total - prev - 1
            # 오른쪽 부모가 있다면
            if (total - prev) <= right <= (total - 1):
                plus = d[right] + num
                d[i + total] = max(plus, d[i + total])
            # 왼쪽 부모가 있다면
            if (total - prev) <= left <= (total - 1):
                plus = d[left] + num
                d[i + total] = max(plus, d[i + total])
            
    # 마지막 줄의 최대가 답
    for i in range(len(triangle)):
        answer = max(answer, d[total + i])
    return answer