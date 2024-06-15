a=eval(input())
b=eval(input())
if a<0 or b<0:
    print("illegal data")
elif a==b and a>0 and b>0:
    print("It's a square")
elif a!=b and a>0 and b>0:
    print("It's a rectangle")
else:
    print("illegal data")

