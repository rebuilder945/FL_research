chang=eval(input())
kuan=eval(input())
if chang==kuan:
    print("It's a square")
elif chang<0 or kuan<0:
    print("illegal data")
elif chang!=0 and kuan!=0:
    print("It's a rectangle")
