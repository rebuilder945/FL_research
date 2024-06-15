tempstr=input()
if tempstr[0] in ['$','U']:
    if tempstr[0]=='$':
        r=eval(tempstr[1,len(tempstr)+1])*6.78
        print('&%.2f'%r)
    else:
        r=eval(tempstr[3,len(tempstr)+1])*6.78
        print('RMB%.2f'%r)
elif tempstr[0] in ['&','R']:
    if tempstr[0]=='&':
        r=eval(tempstr[1,len(tempstr)+1])/6.78
        print('$%.2f'%m)
    else:
        r=eval(tempstr[3,len(tempstr)+1])/6.78
        print('USD%.2f'%m)
else:
    print('Error')
