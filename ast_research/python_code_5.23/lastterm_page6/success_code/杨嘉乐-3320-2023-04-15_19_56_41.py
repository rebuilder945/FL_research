x=eval(input())
y=eval(input())
if x<=0 or y<=0:
    print("illegal data")
if x>0 and y>0:
    if x==y:
        print("It's a square")
    elif x!=y:
        print("It's a rectangle")


