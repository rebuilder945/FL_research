a=input()
if a[0] in ['&']:
    M=eval(a[1:])/6.78
    print('$%.2f'%M)
elif a[0:3]=='RMB':
    D=eval(a[4:])/6.78
    print('USD%.2f'%D)
elif a[0] in ['$']:
    R=eval(a[1:])*6.78
    print('&%.2f'%R)
elif a[0:3]=='USD':
    B=eval(a[4:])*6.78
    print('RMB%.2f'%B)
else:
    print("error")
