l1 = float(input())
l2 = float(input())
if l1<0 or l2<0:
    print("illegal data")
else:
    if l1 == l2:
        print("It's a square")
    elif l1!=l2:
        print("It's a rectangle")
