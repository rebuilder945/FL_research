a=input()
if a[0]in['&']:
    print('$'+'%.2f'%a/6.78)
elif a[0:3]in['RMB']:
    print('USD'+'%.2f'%a/6.78)
elif a[0]in['$']:
    print('&'+'%.2f'%a*6.78)
elif a[0:3]in['USD']:
    print('RMB'+'%.2f'%a*6.78)
else:
    print('error')
