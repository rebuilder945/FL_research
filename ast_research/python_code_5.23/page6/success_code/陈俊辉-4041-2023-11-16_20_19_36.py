lenth=eval(input())
wide=eval(input())
if lenth==wide:
    print("It's a square")
elif lenth!=wide:
    print("It's a rectangle")
elif lenth<0 or wide<0:
    print("illegal data")
    
