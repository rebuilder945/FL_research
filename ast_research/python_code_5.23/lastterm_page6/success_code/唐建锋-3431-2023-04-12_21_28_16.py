n=int(input())
if n<0 or n>36:
    print("error")
elif 1<=n<=10 and n%2==0:
    print("black")
elif 1<=n<=10 and n%2!=0:
    print("red")
elif 11<=n<=18 and n%2==0:
    print("red")
elif 11<=n<=18 and n%2!=0:
    print("black")
elif 19<=n<=28 and n%2==0:
    print("black")
elif 19<=n<=28 and n%2!=0:
    print("red")
elif 29<=n<=36 and n%2==0:
    print("red")
elif 29<=n<=36 and n%2!=0:
    print("black")
elif n==0:
    print("green")
