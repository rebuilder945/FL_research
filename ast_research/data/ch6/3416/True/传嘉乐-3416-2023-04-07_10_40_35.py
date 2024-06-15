a=input()
if a[0]in['&']:
    b=float(a[1:])
    print('$'+'%.2f'%(b/6.78))
elif a[0:3]in['RMB']:
    b=float(a[3:])
    print('USD'+'%.2f'%(b/6.78))
elif a[0]in['$']:
    b=float(a[1:])
    print('&'+'%.2f'%(b*6.78))
elif a[0:3]in['USD']:
    b=float(a[3:])
    print('RMB'+'%.2f'%(b*6.78))
else:
    print('Error')
