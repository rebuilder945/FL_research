m=input()
if m[0] in'$':
    c=eval(m[1:])*6.78
    print('&%.2f'%c)
elif m[0:3]=='USD':
    c=eval(m[4:])*6.78
    print('RMB%.2f'%c)
elif m[0] =='&':
    c=eval(m[1:])/(6.78)
    print('$%.2f'%c)
elif m[0:3]=='RMB':    
    c=eval(m[4:])/(6.78)
    print('USD%.2f'%c)
else:
    print('Error')

