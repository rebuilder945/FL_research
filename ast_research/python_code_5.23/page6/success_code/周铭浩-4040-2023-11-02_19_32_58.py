x=input()
if x[0] in 'R':
    x=int(x[3:])
    y=x/6.78
    print('USD%.2f'%(y))
elif x[0] in "&":
    x=int(x[1:])
    y=X/6.78
    print('$%.2f'%(y))
elif x[0] in '$':
    x=int(x[1:])
    y=x*6.78
    print('&%.2f'%(y))
else:
    x=int(x[3:])
    y=x*6.78
    print('RMB%.2f'%(y))
