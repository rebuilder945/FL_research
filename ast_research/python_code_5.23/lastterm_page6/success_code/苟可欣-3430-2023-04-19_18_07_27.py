x=eval(input())
if x in range(3,6):
    print("spring")
elif x in range(6,9):
    print("summer")
elif x in range(9,12):
    print("autumn")
elif x in range(1,3) or x==12:
    print("winter")
else:
    print("error")
