n=input()
if n[0]=='$':
    m=eval(n[1:])*6.78
    print('&%.2f'%(m))
elif n[0]=='U':
    m=eval(n[3:])*6.78
    print('RMB%.2f'%(m))
elif n[0]=='&':
    m=eval(n[1:])/6.78
    print('$%.2f'%(m))
elif n[0]=='R':
    m=eval(n[3:])/6.78
    print('USD%.2f'%(m))
else:
    print('error')
