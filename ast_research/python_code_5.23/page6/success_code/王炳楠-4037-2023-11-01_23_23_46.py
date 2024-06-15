n=eval(input())
if n in range(3,6):
    print("spring")
elif n in range(6,9):
    print("summer")
elif n in range(9,12):
    print("autumn")
elif n in [12,1,2]:
    print("winter")
else:
    print("error")
