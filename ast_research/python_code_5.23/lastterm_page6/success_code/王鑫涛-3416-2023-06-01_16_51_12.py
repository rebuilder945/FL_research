a=input()
if a.startswith('USD'):
    b=eval(a[4:])*6.78
    print('RMB%.2f'%b)
elif a.startswith('$'):
    b=eval(a[2:])*6.78
    print('&%.2f'%b)
elif a.startswith('RMB'):
    b=eval(a[4:])/6.78
    print('USD%.2f'%b)
elif a.startswith('&'):
    b=eval(a[2:])/6.78
    print('$%.2f'%b)
else:
    print('Error')
