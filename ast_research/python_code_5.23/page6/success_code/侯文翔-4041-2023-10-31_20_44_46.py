a=int(input())
b=int(input())
if a>0 and b>0 and a==b:
    print("It's a square")
elif  a>0 and b>0 and a!=b:
    print("It's a rectangle")
elif a<0 or b<0:
    print("illegal data")
else:
    pass
