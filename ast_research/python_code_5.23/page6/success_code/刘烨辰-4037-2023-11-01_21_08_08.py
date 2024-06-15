n=eval(input())
if 1<=n<=12:
    if n==3 or n==4 or n==5:
        print('spring')
    elif n==6 or n==7 or n==8:
        print('summer')
    elif n==9 or n==10 or n==11:
        print('autumn')
    else:
        print('winter')
else:
    print('error')
