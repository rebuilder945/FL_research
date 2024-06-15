l=eval(input())
h=eval(input())
if l<0 or h <0:
    print("illegal data")
elif l>0 and h>0 and l==h:
    print("It's a square")
elif l>0 and h>0 and l!=h:
    print("It's a rectangle")


