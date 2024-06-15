a = eval(input())
if a==0:
    print("green")
elif a>=1 and a<=10:
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
elif a<=36:
    if a%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")


