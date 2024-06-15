len=int(input())
k=int(input())
if len<=0 or k <=0:
    print("illegal data")
elif len==k:
    print("It's a square")
elif len !=k:
    print("It's a rectangle")
