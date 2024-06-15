n = eval(input())
if n < 0 or n >36:
    print('error')
else:
    if n == 0:
        print('green')
    elif 0 < n <11 or 18<n<29:
        if n % 2 == 0:
            print('black')
        else:
            print('red')
    else:
        if n % 2 == 0:
            print('red')
        else:
            print('black')
    
