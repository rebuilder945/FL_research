a = eval(input())
b = eval(input())
if a < 0 or b < 0:
    print('illegal date')
else:
    if a == b:
        print("It's a square")
    if a != b:
        print("It's a rectangle")
