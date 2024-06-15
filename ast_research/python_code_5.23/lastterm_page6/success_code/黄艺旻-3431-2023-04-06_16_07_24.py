a=eval(input())
if a not in range(37):
    print('error')
elif a in range(1,11):
    if a%2!=0:
        print('red')
    else:
        print('black')
elif a in range(11,19):
    if a%2!=0:
        print('black')
    else:
        print('red')
elif a in range(19,29):
    if a%2!=0:
        print('red')
    else:
        print('black')
elif a == 0:
    print('green')
else:
    if a%2!=0:
        print('black')
    else:
        print('red')
