a=eval(input())
if a not in range(0,36):
    print("error")
else:
    if a in range(1,10,2):
        print("red")
    elif a in range(2,10,2):
        print("black")
    elif a in range(11,18,2):
        print("black")
    elif a in range(12,18,2):
        print("red")
    elif a in range(19,28,2):
        print("red")
    elif a in range(19,28,2):
        print("black")
    elif a in range(29,36,2):
        print("black")
    elif a in range(29,36,2):
        print("red")
    else:
        print("green")
