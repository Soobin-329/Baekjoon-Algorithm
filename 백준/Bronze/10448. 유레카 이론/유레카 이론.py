# 유레카 이론
# 브론즈 1

import sys
input = sys.stdin.readline

test = int(input())

inputs = []
dp = []
for _ in range(test):
    inputs.append(int(input()))

# 삼각수 표 구하기
max_input = max(inputs)
for i in range(1, max_input):
    triangle_num = i*(i+1)/2

    if triangle_num > max_input:
        break
    dp.append(triangle_num)

# 각 테스트케이스가 3개의 삼각수의 합으로 표현되는지 판단
for i in inputs:
    result = 0
    # 자기보다 작은 삼각수 표에서 3개를 뽑아서 합
    for a in dp:
        if a >= i or result == 1:
            break
        for b in dp:
            if result == 1 or b >= i:
                break
            for c in dp:
                if c < i:
                    if a + b + c == i:
                        result = 1
                        break

    print(result)