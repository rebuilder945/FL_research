a=eval(input())
if a in range(3,6):
    print("spring")
elif a in range(6,9):
    print("summer")
elif a in range(9,12):
    print("autumun")
elif a in range(1,3) or a==12:
    print("winter")
else:
    print("error")
