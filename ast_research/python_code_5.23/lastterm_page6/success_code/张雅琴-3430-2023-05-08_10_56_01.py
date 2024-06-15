a=eval(int(input()))
if a<1 or a>12:
    print("error")
else:
    if a==3 or a==4 or a==5:
        print("spring")
    elif a==6 or a==7 or a==8:
        print("summer")
    elif a==9 or a==10 or a==11:
        print("autumn")
    else:
        print("winter")

