a=input()
if a.startswith('USD'):
    b=a[4:]*6.78
    print('RMB%.2f'%b)
if a.startswith('$'):
    b=a[4:]*6.78
    print('&%.2f'%b)
if a.startswith('RMB'):
    b=a[4:]/6.78
    print('USD%.2f'%b)
if a.startswith('&'):
    b=a[4:]/6.78
    print('$%.2f'%b)
