str=input()
if str[0] in ['$']:
    c=(eval(str[1:]))*6.78
    print('&%.2f'%c)
elif str[0] in ['U']:
    c=(eval(str[3:]))*6.78
    print('RMB%.2f'%c)
elif str[0] in ['&']:
    f=(eval(str[1:]))/6.78
    print('$%.2f'%f)
elif str[0] in ['R']:
    c=(eval(str[3:]))/6.78
    print('USD%.2f'%c)
else:
    print('Error')
