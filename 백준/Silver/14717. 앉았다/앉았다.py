a, b = map(int, input().split())
total = 9*17
win = 0

# 땡 일때 확률
if a == b:
    win = total - (10 - a)
# 끗 일때 확률
else:
    player = (a+b) % 10
    # 1-10의 카드 두 세트
    for i in range(1, 11):
        for j in range(i+1, 11):
            # 영학이가 이겼을 때
            if player > (i+j) % 10:
                # 영학이가 뽑은 카드는 제외
                if i == a and j == b:
                    continue
                # 겹치는 카드가 있다면 이기는 경우의 수 2
                # 예를 들어, (1 3), (3, 1). 만 가능
                elif i == a or j == a or i == b or j == b:
                    win += 2
                # 겹치는 카드 없으면 이기는 경우의 수 4
                # 예를 들어, ((3 4), (4 3))x 2. 두 세트의 카드는 구별되므로
                else:
                    win += 4

print("%.3f" % (win / total))
