MoneStr = input()
if MoneStr[0]in['$']:
    R = (eval(MoneStr[1::1]))*6.78
    print("&%.2f"%R)
elif MoneStr[0] in ['&']:
    U = (eval(MoneStr[1::1]))/6.78
    print("$%.2f"%U)
elif MoneStr[0:3]in['USD']:
    R = (eval(MoneStr[3::1]))*6.78
    print("RMB%.2f"%R)
elif MoneStr[0:3]in['RMB']:
    U = (eval(MoneStr[3::1]))/6.78
    print("USD%.2f"%U)
else:
    print("Error")


