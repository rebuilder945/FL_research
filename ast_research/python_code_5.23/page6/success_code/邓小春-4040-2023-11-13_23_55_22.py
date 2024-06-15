a=input()
if a[0] in ['$']:
    t=(eval(a[1: ]))*6.78
    print('&%.2f'%t)
elif a[0:3] in ['USD']:
    t=(eval(a[3: ]))*6.78
    print('RMB%.2f'%t)
elif a[0] in ['&']:
    t=(eval(a[1: ]))/6.78
    print('$%.2f'%t)
elif a[0:3] in ['RMB']:
    t=(eval(a[3: ]))/6.78
    print('USD%.2f'%t)
else:
    print('Error')
