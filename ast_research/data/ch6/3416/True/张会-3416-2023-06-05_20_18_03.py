s=input()
if s[0]=='$':
    a=float(s[1:])
    b=a*6.78
    print('&%.2f'%b)
elif s[0:3]=='USD':
    a=float(s[3:])
    b=a*6.78
    print('RMB%.2f'%b)
elif s[0]=='&':
    a=float(s[1:])
    b=a/6.78
    print('$%.2f'%b)
elif s[0:3]=='RMB':
    a=float(s[3:])
    b=a/6.78
    print('USD%.2f'%b)
else:
    print('Error')
