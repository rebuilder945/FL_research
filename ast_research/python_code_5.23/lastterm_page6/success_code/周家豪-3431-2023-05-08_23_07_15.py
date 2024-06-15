n=int(input())
if n<0 or n>36:
    print('error')
elif 1<=n<=10:
    if n%2==1:
        print('red')
    else:
        print('black')
elif 11<=n<=18:
    if n%2==1:
        print('black')
    else:
        print('red')
elif 19<=n<=28:
    if n%2==1:
        print('red')
    else:
        print('black')
elif 29<=n<=36:
    if n%2==1:
        print('black')
    else:
        print('red')
else:
    print('green')
