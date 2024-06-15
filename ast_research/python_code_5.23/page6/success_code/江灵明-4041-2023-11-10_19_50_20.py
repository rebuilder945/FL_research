l = int(input())
r = int(input())
if l<0 or r <0:
    print("illegal data")
elif l == r and l>0 and r>0:
    print("It's a square")
elif l!=r:
    print("It's a rectangle")
