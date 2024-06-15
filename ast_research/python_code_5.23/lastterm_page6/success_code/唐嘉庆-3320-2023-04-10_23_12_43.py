length=eval(input())
wide=eval(input())
if length>=0 and wide>=0 and length==wide :
    print("It's a square")
if length<0 or wide<0:
    print("illegal data")
if length>=0 and wide>=0 and length!=wide:
    print("It's a rectangle")
