s=eval(input())
if s==0:
    print('green')
elif s in range(1,11):
    if s%2==0:
        print('black')
    else:
        print('red')
elif s in range(11,19):
    if s%2==0:
        print('red')
    else:
        print('black')
elif s in range(19,29):
    if s%2==0:
        print('black')
    else:
        print('red')
elif s in range(29,37):
    if s%2==0:
        print('red')
    else:
        print('black')
else:
    print('error')
