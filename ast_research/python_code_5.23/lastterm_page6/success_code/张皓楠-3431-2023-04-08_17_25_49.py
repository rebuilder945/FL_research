a = eval(input)
if a == 0:
    print("green")
elif 0 < a < 11:
    if a%2:
        print("red")
    else:
        print("black")
elif 10 < a < 19:
    if not a%2:
        print("red")
    else:
        print("black")
elif 18 < a < 29:
    if a%2:
        print("red")
    else:
        print("black")
elif 28 < a < 37:
    if not a%2:
        print("red")
    else:
        print("black")
else:
    print("error")
