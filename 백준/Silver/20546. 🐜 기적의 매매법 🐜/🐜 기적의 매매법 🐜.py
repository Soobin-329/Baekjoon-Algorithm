# 기적의 매매법
# 실버 5


def bnp(money, prices):
    # 준현이의 장기투자
    # 주식을 살 수 있을 때 즉시 매수
    # 팔지 않음
    num_of_stock = 0
    for price in prices:
        if money >= price:
            num_of_stock = money // price
            money = money % price

    return num_of_stock * prices[-1] + money


def timing(money, prices):
    # 성민이의 33투자
    # 전량 매도와 전량 매수
    rise_day = 0
    fall_day = 0
    num_of_stock = 0
    previous_price = 0

    for i, price in enumerate(prices):
        # 첫날은 비교할 전 가격이 없으므로 따로 처리
        if i == 0:
            previous_price = price

        # 오르는지 아닌지 체크
        if price > previous_price:
            fall_day = 0
            rise_day += 1
        elif price < previous_price:
            fall_day += 1
            rise_day = 0
        elif price == previous_price:
            fall_day = 0
            rise_day = 0

        # 3일 연속 오르면 매도
        if rise_day >= 3:
            money += num_of_stock * price
            num_of_stock = 0

        # 3일 연속 내리면 매수
        if fall_day >= 3:
            num_of_stock += money // price
            money = money % price

        previous_price = price

    return num_of_stock * prices[-1] + money


a = int(input())
arr = list(map(int, input().split()))

bnp = bnp(a, arr)
timing = timing(a, arr)

# 출력
if bnp > timing:
    print("BNP")
elif timing > bnp:
    print("TIMING")
else:
    print("SAMESAME")