a = eval(input())
if a>=3 and a<=5:
    print("spring")
elif a>=6 and a<=8:
    print("summer")
elif a>=9 and a<=11:
    print("autumn")
elif a in [12,1,2]:
    print("winter")
else:
    print("error")
