a=eval(input())
if a>0 and a<10:
    if a %2==0:
        print("black")
    else:
        print("red")
if a<19:
    if a%2==0:
        print("red")
    else:
        print("black")
if a <29:
    if a%2==0:
        print("black")
    else:
        print("red")
if a <37:
    if a%2==0:
        print("red")
    else:
        print("black")
if a==0:
    print("green")
elif a<0 or a>=37:
    print("error")
