long=eval(input())
wide=eval(input())
if long>0 and wide >0:
    if long==wide:
        print("It's a square")
    elif long!=wide:
        print("It's a rectangle")
else:
    print("illegal data")
