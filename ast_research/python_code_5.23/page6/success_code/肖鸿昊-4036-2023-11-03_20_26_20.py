a=eval(input())
if a==0:
    print("green")
if a>36:
    print("error")
    if a%2==0 and a<=36:
        if a<=10:
            print("black")
        elif a<=18:
            print("red")
        elif a<=28:
            print("black")
        else:
            print("red")
    else:
        if a<=10:
            print("red")
        elif a<=18:
            print("black")
        elif a<=28:
            print("red")
        else:
            print("black")
