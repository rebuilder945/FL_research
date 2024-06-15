TempStr = input()
if TempStr[0:1] in ['&']:
    U1= (eval(TempStr[1:]) )/6.78
    print('$%.2f'%(U1))
elif TempStr[0:3] in ['RMB']:
    U2= (eval(TempStr[3:]) )/6.78
    print('USD%.2f'%(U2))
elif TempStr[0:1] in ['$']:
    R1= (eval(TempStr[1:]))*6.78
    print('&%.2f'%(R1))
elif TempStr[0:3] in ['USD']:
    R2= (eval(TempStr[3:]))*6.78
    print('RMB%.2f'%(R2))
else:
    print("Error")

