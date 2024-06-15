a=eval(input())
if a==0:
    print('green')

elif 0<a<=36:
    if a in range(10+1):
        if a%2==0:
            print('black')
        else:
            print('red')
    if a in range(11,19):
        if a%2==0:
            print('red')
        else:
            print('black')
    if a in range(19,29):
        if a%2==0:
            print('black')
        else:
            print('red')
    if a in range(29,36+1):
        if a%2==0:
            print('red')
        else:
            print('black')
else:
    print('error')
