a = int(input())
if a<6 and a>1:
    print("spring")
elif a<9 and a>5:
    print("summer")
elif a<12 and a>8:
    print("autumn")
elif a == 12 or a == 1 or a == 2:
    print("winter")
else:
    print("error")
