n = eval(input())
if n>36 or n<0:
    print("error")
elif n%2==0:
    if n == 0:
        print("green")
    elif 1<=n<=10 or 19<=n<=28:
        print("black")
    else:
        print("red")
else:
    if 1<=n<=10 or 19<=n<=28:
        print("red")
    else:
        print("black")









