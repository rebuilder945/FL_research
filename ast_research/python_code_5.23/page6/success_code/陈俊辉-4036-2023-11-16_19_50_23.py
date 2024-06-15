n=eval(input())
if 1<=n<=10 and n%2!=0:
    print("red")
elif 1<=n<=10 and n%2==0:
    print("black")
elif 11<=n<=18 and n%2!=0:
    print("black")
elif 11<=n<=18 and n%2==0:
    print("red")
elif 19<=n<=28 and n%2!=0:
    print("red")
elif 19<=n<=28 and n%2==0:
    print("black")
elif 29<=n<=36 and n%2!=0:
    print("black")
elif 29<=n<=36 and n%2==0:
    print("red")
elif n==0:
    print("green")
else:
    print("error")
