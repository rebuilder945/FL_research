t=input()
if t[0] in ['$']:
    c=(eval(t[1:]))*6.78
    print('&%.2f'%c)
elif t[0 in ['U']]:
    c=(eval(t[3:]))*6.78
    print('RMB%.2f'%c)
elif t[0] in ['&']:
    c=(eval(t[1:]))/6.78
    print('$%.2f'%c)
elif t[0 in ['R']]:
    c=(eval(t[3:]))/6.78
    print('USD%.2f'%c)
else:
    print('error')
