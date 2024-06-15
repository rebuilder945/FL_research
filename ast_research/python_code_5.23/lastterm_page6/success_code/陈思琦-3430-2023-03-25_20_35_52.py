a=eval(input())
if a not in range(1,12):
    print("error")
else:
    if a in range(3,5):
        print("spring")
    elif a in range(6,8):
        print("summer")
    elif a in range(9,12):
        print("autumn")
    else:
        print("winter")
