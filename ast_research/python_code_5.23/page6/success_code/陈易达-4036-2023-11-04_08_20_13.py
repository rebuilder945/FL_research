n = eval(input())
if n < 0 or n > 36:
    print("error")
else:
    if n == 0:
        print("green")
    if 0<n<11:
        if n%2 == 0:
            print("black")
        else:
            print("red")
    if 10<n<19:
        if n%2 == 0:
            print("red")
        else:
            print("black")
    if 18<n<29:
        if n%2 == 0:
            print("black")
        else:
            print("red")
    if 28<n<37:
        if n%2 == 0:
            print("red")
        else:
            print("black")
