m=input()
if m[0] in ['$']:
    c=eval(m[1:-1])*6.78
    print('&%.2f'%c)
elif m[0] in ['USD']:
    c=eval(m[1:-1])*6.78
    print('"RMB"%.2f'%c)
elif m[0] in ['&']:
    c=eval(m[1:-1])/6.78
    print('$%.2f'%c)
elif m[0] in ['RMB']:    
    c=eval(m[1:-1])/6.78
    print('"USD"%.2f'%c)


