def solution(money):    
    n = len(money)
    
    # 첫집을 털지 않고 마지막 집을 무조건 털기
    dp1 = [0] * n  
    dp1[0], dp1[1] = 0, money[1]
            
    for i in range(2, n):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
    
    # 마지막 집을 털지 않고 첫 집을 무조건 털기
    dp2 = [0] * n  
    dp2[0], dp2[1] = money[0], max(money[1], money[0])
            
    for i in range(2, n-1):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
        
    dp2[n-1] = max(dp2[n-2], dp2[n-3])
        
    return max(dp1[-1], dp2[-1])