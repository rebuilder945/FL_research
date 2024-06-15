c = eval(input())
k = eval(input())
if c == k and c>0 and k>0:
    print("It's a square")
elif c <=0 or k<=0:
    print("illegal data")
elif c!=k:
    print("It's a rectangle")
