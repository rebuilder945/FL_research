n = int(input())
if n == 0:
    print("green")
elif 1 <= n <= 10:
    if n % 2 != 0:
        print("red")
    else:
        print("black")
elif 11 <= n <= 18:
    if n % 2 != 0:
        print("black")
    else:
        print("red")
elif 19<= n <= 28:
    if n % 2 != 0:
        print("red")
    else:
        print("black")
elif 29<= n <= 36:
    if n % 2 != 0:
        print("black")
    else:
        print("red")
else:
    print("error")
