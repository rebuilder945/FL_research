n=int(input())
if n<1 or n>12:
    print("error")
elif n in range(3,6):
    print("spring")
elif n in range(6,9):
    print("summer")
elif n in range(9,12):
    print("autumn")
else:
    print("winter")
