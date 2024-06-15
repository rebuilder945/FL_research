month=eval(input())
if 3<=month<=5 and type(month)==int:
    print("spring")
elif 6<=month<=8 and type(month)==int:
    print("summer")
elif 9<=month<=11 and type(month)==int:
    print("autumn")
elif month==1 or month==2 or month== 12:
    print("winter")
else:
    print("error")
