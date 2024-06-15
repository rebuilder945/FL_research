l=eval(input())
w=eval(input())
if l>0 and w>0:
    if l==w:
        print("It's a square")
    elif l!=w:
        print("It's a rectangle")
elif l<0 or w<0:
   print("illegal data")
