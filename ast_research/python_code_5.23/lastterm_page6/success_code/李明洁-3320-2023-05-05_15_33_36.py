n = input()
m = input()
if n == m:
    print("It's a square")
elif n != m:
    print("It's a rectangle")
else:
    if n<0 or m<0:
        print("illegal data")
