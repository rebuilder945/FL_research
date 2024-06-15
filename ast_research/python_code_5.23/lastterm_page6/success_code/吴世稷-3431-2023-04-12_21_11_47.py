n = eval(input())
if n == 0:
    print('green')
elif 1<=n<=10:
    if n==1 or n==3 or n==5 or n==7 or n==9:
        print('red')
    else:
        print('black')
elif 11<=n<=18:
    if n==12 or n==14 or n==16 or n==18:
        print('red')
    else:
        print('black')
elif 19<=n<=28:
    if n==19 or n==21 or n==23 or n==25 or n==27:
        print("red")
    else:
        print('balck')
elif 29<=n<=36:
    if n==30 or n==32 or n==34 or n==36:
        print('red')
    else:
        print('black')
else:
    print('error')
