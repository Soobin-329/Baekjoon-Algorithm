from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    number_list = []
    
    for i in range(1, len(numbers) + 1):
        permuts = permutations(numbers, i)
        
        # ('1','0','1') -> 101
        for p in list(permuts):
            string = "".join(p)
            number_list.append(int(string))
        
    number_set = set(number_list)
    arr = list(number_set)
    print(arr)
    
    # 소수인지 판별
    for a in arr:
        # 0, 1 은 소수 아님
        if a <= 1:
            continue
            
        flag = True
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                flag = False
                break
        # 소수라면 answer 증가
        if flag:
            print("소수임둥", a)
            answer += 1
    
    return answer