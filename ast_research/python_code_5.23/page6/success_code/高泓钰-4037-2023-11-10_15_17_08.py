s=eval(input())
if 1<=s<=12:
    if s==3 or s==4 or s==5:
        print("spring")
    elif s==6 or s==7 or s==8:
        print("summer")
    elif s==9 or s==10 or s==11:
        print("autumn")
    else:
        print("winter")
else:
    print("error")
