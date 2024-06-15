a = int(input())
if a < 0 or a > 36:
    print("error")
elif a == 0:
    print("绿色")
elif a >= 1 and a <= 10:
    if a % 2 ==0:
        print("黑色")
    else:
        print("红色")
elif a >= 11 and a <= 18:
    if a % 2 ==0:
        print("红色")
    else:
        print("黑色")
elif a >= 19 and a <=28:
    if a % 2 ==0:
        print("黑色")
    else:
        print("红色")
elif a >= 29 and a <= 36:
    if a % 2 ==0:
        print("红色")
    else:
        print("黑色")
