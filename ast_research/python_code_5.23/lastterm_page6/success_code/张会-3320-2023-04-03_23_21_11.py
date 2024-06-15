chang = eval(input())
kuan = eval(input())
if chang <=0 or kuan <=0:
    print("illegal data")
else:
    if chang == kuan:
        print("It's a square")
    elif chang!=kuan:
        print("It's a rectangle")

