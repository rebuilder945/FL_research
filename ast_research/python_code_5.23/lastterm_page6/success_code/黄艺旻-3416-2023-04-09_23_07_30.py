m=eval(input())
if m[0]=='$':
    R=m*6.78
    print('&%.2f'%R)
elif m[0]=='&':
    M=m/6.78
    print('$%.2f'%M)
elif m[0:3]=='USD':
    r=m*6.78
    print('RMB%.2f'%r)
elif m[0:3]=='RMB':
    u=m*6.78
    print('USD%.2f'%u)
