a = input()
if a[0] == '$':
    b = (eval(a[1:]))*6.78
    c = '&' + str(b)
    print(c)
elif a[0] == '&':
    b = (eval(a[1:]))/6.78
    c = '$' + str(b)
    print(c)
elif a[0] == 'RMB':
    b = (eval(a[1:]))*6.78
    c = 'USD' + str(b)
    print(c)
elif a[0] == 'USD':
    b = (eval(a[1:]))/6.78
    c = 'RMB' + str(b)
    print(c)
else:
    print('error')


