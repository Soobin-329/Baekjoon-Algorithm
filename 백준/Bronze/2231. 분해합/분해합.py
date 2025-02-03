# 분해합
# 브론즈 2

def f_hap(n):
    hap = n
    nstr = str(n)

    for s in nstr:
        hap += int(s)
    return hap


num = int(input())
flag = True

for i in range(1, num + 1):
    if f_hap(i) == num:
        print(i)
        flag = False
        break

if flag:
    print(0)