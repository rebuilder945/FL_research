a=eval(input())
if a<0 or a>36:
    print("error")
else:
    if a==0:
        print("green")
    elif a>0 and a%2==0:
        if 1<=a<=10 or 19<=a<=28:
            print("black")
        else:
            print("red")
    elif a>0 and a%2!=0:
        if 1<=a<=10 or 19<=a<=28:
            print("red")
        else:
            print("black")
