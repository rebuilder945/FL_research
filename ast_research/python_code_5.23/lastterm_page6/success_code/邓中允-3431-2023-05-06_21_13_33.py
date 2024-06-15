n=eval(input())
if n<0 or n>36:
    print("error")
elif 1<=n<=10:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 11<=n<=18:
    if n%2==0:
        print("red")
    else:
        print("black")
elif 19<=n<=28:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 29<=n<=36:
    if n%2==0:
        print("red")
    else:
        print("black")
else:
    print("green")
