n=int(input())
if n < 0 or n >36:
    print('error')
elif n == 0:
    print('green')
else:
    if n in range(1,11) or n in range(19,29):
        if n % 2 ==0:
            print('black')
        else:
            print('red')
    else:
        if n % 2 ==0:
            print('red')
        else:
            print('black')
