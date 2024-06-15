n=eval(input())
a='black'
b='red'
if n==0:
    print('green')
elif 1<=n<=10:
    if n%2==0:
        print(a)
    else:
        print(b)
elif 11<=n<=18:
    if n%2==0:
        print(b)
    else:
        print(a)
elif 19<=n<=28:
    if n%2==0:
        print(a)
    else:
        print(b)
elif 29<=n<=36:
    if n%2==0:
        print(b)
    else:
        print(a)
else:
    print('error')
