a = int(input())
if a<0 or a>36:
    print("error")
else:
    if a==0:
        print("green")
    elif 1<=a<=10 or 19<=a<=28:
        if a%2!=0:
            print("red")
        else:
            print("black")
    else:
        if a%2!=0:
            print("black")
        else:
            print("red")
