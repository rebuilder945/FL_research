c = eval(input())
k = eval(input())
if c>0 and k>0:
    if c == k:
        print("It's a square")
    elif c != k:
        print("It's a rectangle")
elif c<0 or k<0:
    print("illegal data")
