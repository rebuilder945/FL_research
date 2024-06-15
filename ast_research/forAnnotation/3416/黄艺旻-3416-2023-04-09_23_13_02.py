m=input()
if m[0]=='$':
    R=eval(m[1:])*6.78
    print('&%.2f'%R)
elif m[0]=='&':
    M=eval(m[1:])/6.78
    print('$%.2f'%M)
elif m[0:3]=='USD':
    r=eval(m[3:])*6.78
    print('RMB%.2f'%r)
elif m[0:3]=='RMB':
    u=eval(m[3:])*6.78
    print('USD%.2f'%u)
