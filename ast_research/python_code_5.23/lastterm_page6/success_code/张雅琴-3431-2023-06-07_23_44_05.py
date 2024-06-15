a=eval(input())
if a<0 or a>36:
    print("error")
elif a==0:
    print("green")
else:
    if 1<a<=10:
        if a%2==0:
            print("black")
        else:
            print("red")
    elif 11<=a<=18:
        if a%2==0:
            print("red")
        else:
            print("black")
    elif 19<=a<=28:
        if a%2==0:
            print("black")
        else:
            print("red")
    else:
        if a%2==0:
            print("red")
        else:
            print("black")

