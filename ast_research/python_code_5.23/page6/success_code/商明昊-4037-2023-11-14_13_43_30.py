n = eval(input())
if n>=3 and n<=5:
    print("spring")
elif n>=6 and n<=8:
    print("summer")
elif n>=9 and n<=11:
    print("autumn")
elif n>12 or n<1:
    print('error')
else:
    print("winter")
