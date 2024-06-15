Month = eval(input())
if Month>12 or Month <=0:
    print("error")
elif Month % 12 <3:
    print("winter")
elif Month % 12 <6:
    print("spring")
elif Month % 12 <9:
    print("summer")
elif Month % 12 <=11:
    print("autumn")
