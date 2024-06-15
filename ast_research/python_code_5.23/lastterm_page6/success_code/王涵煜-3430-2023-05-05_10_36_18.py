a = eval(input())
if a<1 or a>12:
    print("error")
elif a in [3,4,5]:
    print("spring")
elif a in [6,7,8]:
    print("summer")
elif a in [9,10,11]:
    print("autumn")
else:
    print("winter")


