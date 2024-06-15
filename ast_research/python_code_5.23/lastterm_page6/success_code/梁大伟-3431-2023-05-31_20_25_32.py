n=eval(input())
if n in range(1,11):
    if n % 2 ==0:
        print('black')
    else:
        print('red')
elif n in range(11,19):
    if n % 2 ==0:
        print('red')
    else:
        print('black')
elif n in range(19,29):
    if n % 2 ==0:
        print('black')
    else:
        print('red')
elif n in range(29,37):
    if n % 2 ==0:
        print('red')
    else:
        print('black')
elif n == 0:
    print('green')
else:
    print('error')
