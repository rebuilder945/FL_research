n=int(input())
if 1<=n<=10 or 19<=n<=28:
    if n/2!=n//2:
        print("red")
    else:
        print("black")
elif 11<=n<=18 or 29<=n<=36:
    if n/2!=n//2:
        print("black")
    else:
        print("red")
elif n==0:
    print("green")
else:
    print("error")
