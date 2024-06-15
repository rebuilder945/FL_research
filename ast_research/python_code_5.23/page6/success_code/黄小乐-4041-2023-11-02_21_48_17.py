len=int(input())
wide=int(input())
if len<=0 or wide<=0:
    print("illegal data")
elif wide ==len:
    print("It's a square")
elif wide!=len:
    print("It's a rectangle")
