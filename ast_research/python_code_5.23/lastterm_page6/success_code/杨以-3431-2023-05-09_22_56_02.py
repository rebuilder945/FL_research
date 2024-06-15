n=eval(input())
if n==0:
    print('green')
if n in range(1,11) and n%2==0:
    print('black')
if n in range(1,11) and n%2!=0:
    print('red')
if n in range(11,19) and n%2==0:
    print('red')
if n in range(11,19) and n%2!=0:
    print('black')
if n in range(19,29) and n%2==0:
    print('black')
if n in range(19,29) and n%2!=0:
    print('red')
if n in range(29,37) and n%2==0:
    print('red')
if n in range(29,37) and n%2!=0:
    print('black')
if n not in range(0,37):
    print('error')


