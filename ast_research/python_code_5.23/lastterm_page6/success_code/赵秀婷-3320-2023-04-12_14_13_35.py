longth=eval(input())
lenth=eval(input())
if longth==lenth and longth*lenth>0:
    print("It's a square")
if longth!=lenth and longth*lenth>0:
    print("It's a rectangle")
if longth<0 or lenth<0:
    print("illegal data")
