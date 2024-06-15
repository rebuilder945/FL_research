a = eval(input())
if 0<a<11:
    if a%2 == 0:
        print('black')
    else:
        print('red')
elif 10<a<19:
    if a%2 == 1:
        print('black')
    else:
        print('red')
elif 18<a<29:
    if a%2 == 0:
        print('black')
    else:
        print('red')
elif 28<a<37:
    if a%2 == 1:
        print('black')
    else:
        print('red')
else:
    print('error')
