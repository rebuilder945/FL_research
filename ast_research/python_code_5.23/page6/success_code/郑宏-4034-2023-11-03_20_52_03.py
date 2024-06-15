a=input()
b=input()
c=[a,b]
if 'red' in c:
    if 'blue' in c:
        print('purple')
    elif 'yellow' in c:
        print('orange')
    else:
        print('error')
elif 'blue' in c:
    if 'yellow' in c:
        print('green')
    else:
        print('error')
