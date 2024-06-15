height=eval(input())
wide=eval(input())
if height>0 and wide>0 and height==wide:
    print("It's a square")
if height>0 and wide>0 and height!=wide:
    print("It's a rectangle")
if height<0 or wide<0:
    print("illegal data")
