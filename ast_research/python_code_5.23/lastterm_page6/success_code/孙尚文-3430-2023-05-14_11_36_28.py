a=eval(input())
def jijie(b):
    if 3<=b<=5:
        print("spring")
    elif 6<=b<=8:
        print("summer")
    elif 9<=b<=11:
        print("autumn")
    elif b==12 or b==1 or b==2:
        print("winter")
    else:
        print("error")
jijie(a)
