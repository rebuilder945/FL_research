Money=input()
if Money[0] in ['$']:
    a=(eval(Money[1:]))*6.78
    print('&%.2f'%(a))
elif Money[0] in ['&']:
    a=(eval(Money[1:]))%6.78
    print('$%.2f'%(a))
elif Money[0:3] in ['RMB']:
    a=(eval(Money[3:]))%6.78
    print('USD%.2f'%(a))
elif Money[0:3] in ['USD']:
    a=(eval(Money[3:]))*6.78
    print('RMB%.2f'%(a))
else :
    print("Error")
