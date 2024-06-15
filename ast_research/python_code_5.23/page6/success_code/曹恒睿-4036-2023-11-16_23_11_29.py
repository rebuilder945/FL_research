n = eval(input())
if 0 <= n <= 36:
    if 1 <= n <= 10:
        if n % 2 == 0:
            print("black")
        else:
            print("red")
    if 11 <= n <= 18:
        if n % 2 == 0:
            print("red")
        else:
            print("black")
    if 19 <= n <= 28:
        if n % 2 == 0:
            print("black")
        else:
            print("red")
    if 29 <= n <= 36:
        if n % 2 == 0:
            print("black")
        else:
            print("red")
    if n == 0:
        print("green")
else:
    print("error")
