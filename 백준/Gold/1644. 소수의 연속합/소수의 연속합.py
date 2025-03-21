# 소수의 연속합
# 골드 3

import math


def find_primes():
    # 에라토스테네스의 채
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            for j in range(i * 2, n + 1, i):
                arr[j] = False

    arr = [i for i in range(2, n + 1) if arr[i]] # +[0]

    return arr


n = int(input())

primes = find_primes()

# low case도 고려해야함!
if len(primes) == 0:
    print(0)
    exit()

# 투포인터로 경우의 수 구하기
front, back = 0, 0
subtotal = primes[0]
answer = 0

while front <= back < len(primes):
    if subtotal <= n:
        if subtotal == n:
            answer += 1

        back += 1
        if back < len(primes):
            subtotal += primes[back]

    elif subtotal > n:
        subtotal -= primes[front]
        front += 1


print(answer)