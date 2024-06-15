n = eval(input())
if 1 <= n <= 10:
    if n%2 == 0:
        print("black")
    else:
        print("red")
elif 10 < n <= 18:
    if n%2 == 0:
        print("red")
    else:
        print("black")
elif 19<= n <= 28:
    if n%2 == 0:
        print("black")
    else:
        print("red")
elif 29<= n <=36:
    if n%2 == 0:
        print("red")
    else:
        print("black")
elif n == 0:
    print("green")
else:
    print("error")
