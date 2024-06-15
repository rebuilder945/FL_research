a=float(input())
b=float(input())
print(a,b)
if a<0 or b<0:
    print("illegal data")
elif a==b:
    print("It's a square")
else: 
    print("It's a rectangle")
