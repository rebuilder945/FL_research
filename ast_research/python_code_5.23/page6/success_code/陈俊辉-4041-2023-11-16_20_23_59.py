lenth=eval(input())
wide=eval(input())
if lenth<=0 or wide<=0:
    print("illegal data")
elif lenth>0 and wide>0 and lenth==wide:
    print("It's a square")
elif lenth>0 and wide>0 and lenth!=wide:
    print("It's a rectangle")

