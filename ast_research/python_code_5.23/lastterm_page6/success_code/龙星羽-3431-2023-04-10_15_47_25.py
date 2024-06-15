z=eval(input())
if 0<z<=10 or 18<z<=28:
    if z%2==0:
        print('black')
    else:
        print('red')
elif 10<z<=18 or 28<z<=36:
    if z%2==0:
        print('red')
    else:
        print('black')
elif z==0:
    print('green')
else:
    print('error')

