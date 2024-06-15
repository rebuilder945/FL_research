a=["red","blue","yellow"]
b=(input())
c=(input())
if b!=c and b in a and c in a:
    if b==a[0] and c==a[1]:
        print("purple")
    elif b==a[1] and c==a[0]:
        print("purple")
    elif b==a[0] and c==a[2]:
        print("orange")
    elif b==a[2] and c==a[0]:
        print("orange")
    elif b==a[2] and c==a[1]:
        print("green")
    elif b==a[1] and c==a[2]:
        print("green")
    else:
        pass
else:
    print("error")


