TempStr = input()
if TempStr[0] in ['$']:
    RMB = (eval(TempStr[1:]))*6.78
    print("&{:.2f}".format(RMB))
elif TempStr[0] in ['U']:
    RMB = (eval(TempStr[3:]))*6.78
    print("RMB{:.2f}".format(RMB))
elif TempStr[0] in ['&']:
    USD = (eval(TempStr[1:]))/6.78
    print('${:.2f}'.format(USD))    
elif TempStr[0] in ['R']:
    USD = (eval(TempStr[3:]))/6.78
    print('USD{:.2f}'.format(USD))
else:
    print("Error")
    
                

