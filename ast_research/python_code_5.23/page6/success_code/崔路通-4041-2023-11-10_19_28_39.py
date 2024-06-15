L=eval(input())
D=eval(input())
if not (L>0 and D>0):
    print("illegal data")
elif L==D:
    print("It's a square")
else:
    print("It's a rectangle")
