a=input()
b={'USD','RMB'}
c={'&','$'}
if a[0:3] in b:
    d=eval(a[3:])
    
    if a[0:3]=='USD':
        m=d*6.78
        print('RMB%.2f'%(m))
    else:
        m=d/6.78
        print('USD%.2f'%(m))
elif a[0] in c:
    d=eval(a[1:])
    if a[0]=="$":
        m=d*6.78
        print('&%.2f'%(m))
    else:
        m=d/6.78
        print('$%.2f'%(m))
else:
    print('error')

