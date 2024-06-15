n=eval(input())
if n<0 or n>36 or type(n)!=int:
    print('error')
if n==0:
    print('green')
if 1<=n<=10 or 19<=n<=28:
    if n%2==1:
        print('red')
    else:
        print('black')
if 11<=n<=18 or 29<=n<=36:
    if n%2==0:
        print('red')
    else:
        print('black')
