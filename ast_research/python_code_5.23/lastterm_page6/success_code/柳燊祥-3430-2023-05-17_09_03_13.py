m=eval(input())
if m>=3 and m<=5:
    print("spring")
elif m>=6 and m<=8:
    print("summer")
elif m>=9 and m<=11:
    print("autumn")
elif m>=1 and m<=2 or m==12:
    print("winter")
else:
    print("error")
