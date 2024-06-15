n=eval(input())
if n==0:
    print('green')
elif (n>=1 and n<=10) or (n>=19 and n<=28):
    if n%2==0:
        print('black')
    else:
        print('red')
elif (11<=n<=18) or (29<=n<=36):
    if n%2==0:
        print('red')
    else:
        print('black')
else:
    print('error')
