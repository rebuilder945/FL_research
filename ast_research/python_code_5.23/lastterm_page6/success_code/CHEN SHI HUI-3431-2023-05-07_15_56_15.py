def cal(n):
    if n%2==0:
        return True
    return False
n=int(input())
if 1<=n<=10 or 19<=n<=28:
    if cal(n):
        print('black')
    else:
        print('red')
elif 11<=n<=18 or 29<=n<=36:
    if cal(n):
        print('red')
    else:
        print('black')
elif n==0:
    print('green')
else:
    print('error')
