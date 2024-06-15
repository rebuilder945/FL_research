n=eval(input())
if n>=0 and n<=36:
    if n==0:
        print("green")
    elif n>0 and n<=10:
        if n%2==0:
            print("black")
        else:
            print("red")
    elif n>10 and n<=18:
        if n%2==0:
            print("red")
        else:
            print("black")
    elif n>18 and n<=28:
        if n%2==0:
            print("black")
        else:
            print("red")
    elif n>28 and n<=36:
        if n%2==0:
            print("red")
        else:
            print("black")
else:
    print("error")
