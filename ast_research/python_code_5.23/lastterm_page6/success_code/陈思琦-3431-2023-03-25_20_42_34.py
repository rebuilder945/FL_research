a=eval(input())
if a not in range(0,37):
    print("error")
else:
    if a in range(1,11,2):
        print("red")
    elif a in range(2,11,2):
        print("black")
    elif a in range(11,19,2):
        print("black")
    elif a in range(12,19,2):
        print("red")
    elif a in range(19,29,2):
        print("red")
    elif a in range(20,29,2):
        print("black")
    elif a in range(29,37,2):
        print("black")
    elif a in range(30,37,2):
        print("red")
    else:
        print("green")
