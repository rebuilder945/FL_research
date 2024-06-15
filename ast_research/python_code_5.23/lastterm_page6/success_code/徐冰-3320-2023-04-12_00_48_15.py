len=eval(input())
wid=eval(input())
if len <=0 or wid <=0:
    print("illegal data")
else:
    if len==wid:
        print("It's a square")
    else:
        print("It's a rectangle")
