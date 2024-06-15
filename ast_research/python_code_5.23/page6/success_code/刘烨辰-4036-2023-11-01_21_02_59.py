n=eval(input())
if 0<=n<=36:
    if n==0:
        print('green')
    elif n==1 or n==3 or n==5 or n==7 or n==9 or n==12 or n==14 or n==16 or n==18 or n==19 or n==21 or n==23 or n==25 or n==27 or n==30 or n==32 or n==34 or n==36:
        print('red')
    else:
        print('black')
else:
    print('error')
