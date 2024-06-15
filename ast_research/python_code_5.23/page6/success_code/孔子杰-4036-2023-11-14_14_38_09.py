n=eval(input())
if n==0:
    print("green")
elif 1<=n<=10 or 19<=n<=28:
    if n%2!=0:
        print("red")
    elif n%2==0:
        print("black")
elif 11<=n<=18 or 29<=n<=36:
    if n%2!=0:
        print("black")
    elif n%2==0:
        print("red")
else:
    print("error")

