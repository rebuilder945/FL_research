a=eval(input())
if a<0 or a>36:
    print("error")
else:
    if a==0:
        print("green")
    elif (a>0 and a<=10)or(a>18 and a<=28):
        if a%2==0:
            print("black")
        else:
            print("red")
    elif (a>10 and a<=18)or(a>28 and a<=36):
        if a%2==0:
            print("red")
        else:
            print("black")
