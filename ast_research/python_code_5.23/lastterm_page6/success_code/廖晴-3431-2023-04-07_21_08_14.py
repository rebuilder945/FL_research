a=eval(input())
if a==0:
    print("green")
elif a>0 and a<11 or a>18 and a <29:
    if a%2==0:
        print("black")
    else:
        print("red")
elif a>10 and a<19 or a>28 and a<37:
    if a%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")
