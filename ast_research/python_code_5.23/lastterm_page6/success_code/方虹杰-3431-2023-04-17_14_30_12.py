a=int(input())
if a<0 or a>36:
    print("error")
else:
    if a==0:
        print("green")
    elif a<=10:
        if a%2==0:
            print("black")
        else:
            print("red")
    elif a<=18:
        if a%2==0:
            print("red")
        else:
            print("black")
    elif a<=28:
        if a%2==0:
            print("black")
        else:
            print("red")
    else:
        if a%2==0:
            print("red")
        else:
            print("black")
