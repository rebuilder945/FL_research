n=eval(input())
m=eval(input())
if n<0 or m<0:
    print("illegal data")
else:
    if n==m:
        print("It's a square")
    elif n!=m:
        print("It's a rectangle")
    
