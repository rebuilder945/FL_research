a=eval(input())
b=eval(input())
if a<0 or b<0:
    print("illegal data")
elif a>0 and b>0 and a!=b:
    print("It's a rectangle")
elif a>0 and b>0 and a==b:
    print("It's a square")
else:
    print("illegal data")

