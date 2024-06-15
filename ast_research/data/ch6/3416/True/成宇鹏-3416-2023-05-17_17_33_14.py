a = input()
if a[0] == '$':
    b = (eval(a[1:]))*6.78
    print('&%.2f'%b)
elif a[0] == '&':
    b = (eval(a[1:]))/6.78
    print('$%.2f'%b)
elif a[0:3] == 'RMB':
    b = (eval(a[3:]))/6.78
    print('USD%.2f'%b)
elif a[0:3] == 'USD':
    b = (eval(a[3:]))*6.78
    print('RMB%.2f'%b)
else:
    print('Error')


