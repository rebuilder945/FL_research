def bagcolor(a):
    if 1<=a<=10:
        if a%2==0:
            print('black')
        elif a%2==1:
            print('red')
    elif 11<=a<=18:
        if a%2==0:
            print('red')
        elif a%2==1:
            print('black')
    elif 19<=a<=28:
        if a%2==0:
            print('black')
        elif a%2==1:
            print('red')
    elif 29<=a<=36:
        if a%2==0:
            print('red')
        elif a%2==1:
            print('black')
    elif a==0:
        print('green')
    else:
        print('error')
n=eval(input())
bagcolor(n)


