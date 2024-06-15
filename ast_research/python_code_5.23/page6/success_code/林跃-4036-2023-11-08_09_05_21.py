n=eval(input())
if n==0:
    print("greeen")
elif 1<=n<=10 or 19<=n<=28:
    if n%2!=0:
        print("red")
    else:
        print("black")
elif 10<=n<=18 or 29<=n<=36:
    if n%2!=0:
        print("black")
    else:
        print("red")
