lenth=eval(input())
width=eval(input())
if lenth<=0 or width<=0:
    print("illegal data")
elif lenth==width:
    print("It's a square")
elif lenth!=width:
    print("It's a rectangle")
