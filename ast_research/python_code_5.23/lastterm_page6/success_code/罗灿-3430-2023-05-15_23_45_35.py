n=int(input())
if 3<=n<=5:
    print("spring")
elif 6<=n<=8:
    print("summer")
elif 9<=n<=11:
    print("autumn")
elif n in ['12','1','2']:
    print("winter")
else:
    print("error")
