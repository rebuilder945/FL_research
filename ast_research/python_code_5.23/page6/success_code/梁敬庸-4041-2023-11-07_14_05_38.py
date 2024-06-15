len=eval(input())
w=eval(input())
if len<0 or w<0:
    print("illegal data")
else:
    if len==w:
        print("It's a square")
    elif len!=w:
        print("It's a rectangle")
