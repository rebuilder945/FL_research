#月份
a=eval(input())
if a in (3,6):
    print("spring")
elif a in (6,9):
    print("summer")
elif a in (9,12):
    print("autumn")
elif a in (1,3) or (12,13):
    print("winter")
else:
    print("error")

