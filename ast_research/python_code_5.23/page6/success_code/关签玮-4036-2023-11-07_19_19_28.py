a=eval(input())
if a>0 and a<10:
    if a %2==0:
        print("black")
    else:
        print("red")
if a<19 and a>9:
    if a%2==0:
        print("red")
    else:
        print("black")
if a <29 and a>18:
    if a%2==0:
        print("black")
    else:
        print("red")
if a <37 and a>28:
    if a%2==0:
        print("red")
    else:
        print("black")
if a==0:
    print("green")
elif a<0 or a>=37:
    print("error")
