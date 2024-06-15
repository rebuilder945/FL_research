s=float(input())
n=float(input())
if s<0 or n<0:
    print("illegal data")
elif s!=n:
    print("It's a rectangle")
elif s==n and s>=0 and n>=0:
    print("It's a square")
