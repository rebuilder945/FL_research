def monthname(n):
    if 1<=n<=12:
        if 3<=n<=5:
            print('spring')
        elif 6<=n<=8:
            print('summer')
        elif 9<=n<=11:
            print('autumn')
        else:
            print('winter') 
    else:
        print('error')
a=eval(input())
monthname(a)
