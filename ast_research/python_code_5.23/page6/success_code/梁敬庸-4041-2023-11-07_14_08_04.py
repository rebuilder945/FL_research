len=eval(input())
w=eval(input())
if len>0 and w>0:
    if len==w:
        print("It's a square")
    elif len!=w :
        print("It's a rectangle")
else:
    print("illegal data")
