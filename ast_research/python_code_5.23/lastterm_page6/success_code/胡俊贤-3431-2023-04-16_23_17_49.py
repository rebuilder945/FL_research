a=input()
if a==0:
    print('green')
elif a>0 and a<=10:
    if a%2==0:
        print('black')
    else:
        print('red')   
elif a>10 and a<=18:
    if a%2==0:
        print('red')
    else:
        print('black')
elif a>18 and a<=28:
    if a%2==0:
        print('black')
    else:
        print('red')
elif a>28 and a<=36:
    if a%2==0:
        print('red')
    else:
        print('black')
else:
    print('error')
