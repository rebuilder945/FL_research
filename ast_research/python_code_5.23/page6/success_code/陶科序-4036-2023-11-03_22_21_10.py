a = eval(input())
if 0< a <= 10:
    if a % 2 == 0:
        print("black")
    else:
        print("red") 
elif a<= 18:
    if a % 2 == 0:
        print("red")
    else:
        print("black")
elif a <= 28:
    if a % 2 == 0:
        print("black")
    else:
        print("red")
elif a <= 36:
    if a % 2 == 0:
        print("red")
    else:
        print("black")
elif a == 0:
    print("green")
else:
    print("error")
