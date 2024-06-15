a=eval(input())
b=eval(input())
if a<0 or b<0:
    print("illegal data")
elif a>0 and b>0:
    if a==b:
        print("It's a square")
    elif a!=b:
        print("It's a rectangle")


