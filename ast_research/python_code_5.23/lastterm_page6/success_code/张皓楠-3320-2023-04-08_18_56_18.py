a = eval(input())
b = eval(input())
if a == b and a > 0:
    print("It's a square")
elif a <= 0 or b <= 0:
    print("illegal data")
else:
    print("It's a rectangle")
