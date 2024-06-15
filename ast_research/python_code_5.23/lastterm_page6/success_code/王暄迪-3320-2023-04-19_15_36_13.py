lenth=eval(input())
w=eval(input())
if lenth==w and lenth>0 and w>0:
    print("It's a square")
elif lenth<=0 or w<=0:
    print("illegal data")
else:
    print("It's a rectangle")
