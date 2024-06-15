A = int(input())
if A > 36 or A < 0:
    print("error")
elif A >= 1 and A <= 10:
    if A % 2 != 0:
        print("red")
    else:
        print("black")
elif A >= 11 and A <= 18:
    if A % 2 != 0:
        print("black")
    else:
        print("red")
elif A >= 19 and A <= 28:
    if A % 2 != 0:
        print("red")
    else:
        print("black")
elif A >= 29 and A <= 36:
    if A % 2 != 0:
        print("black")
    else:
        print("red")
else:
    print("green")
