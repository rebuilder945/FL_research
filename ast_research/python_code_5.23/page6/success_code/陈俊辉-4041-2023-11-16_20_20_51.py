lenth=eval(input())
wide=eval(input())
if lenth==wide:
    print("It's a square")
elif lenth<0 or wide<0:
    print("illegal data")
elif lenth!=wide:
    print("It's a rectangle")

