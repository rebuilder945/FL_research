tempstr=input()
if tempstr[0] in ['$','U']:
    r=6.78*eval(tempstr[1:len(tempstr)+1])
    if tempstr[0]=='$':
        print('&%.2f'%r)
    else:
        print('RMB%.2f'%r)
elif tempstr[0] in ['&','R']:
    m=eval(tempstr[1:len(tempstr)+1])/6.78
    if tempstr[0]=='&':
        print('$%.2f'%m)
    else:
        print('USD%.2f'%m)
else:
    print('Error')
