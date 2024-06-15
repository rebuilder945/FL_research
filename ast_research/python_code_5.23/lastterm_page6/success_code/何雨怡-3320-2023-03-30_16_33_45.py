length=eval(input())
width=eval(input())
if length<=0 or width<=0:
    print("illegal data")
elif length>0 and width>0:
    if length==width:
        print("It's a square")
    else:
        print("It's a rectangle")
else:
    pass
