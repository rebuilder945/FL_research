n=eval(input())
m=eval(input())
if n<0 or m<0:
    print("illegal data")
if n==m and n>0 and m>0:
    print("It's a square")
if n!=m and n>0 and m>0:
    print("It's a rectangle")
