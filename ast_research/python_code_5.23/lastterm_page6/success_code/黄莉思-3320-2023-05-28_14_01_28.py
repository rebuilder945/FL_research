l=int(input())
w=int(input())
if l <=0 or w<=0:
    print("illegal data")
elif l==w:
    print("It's a square")
elif l<=w:
    print("It's a rectangle")
