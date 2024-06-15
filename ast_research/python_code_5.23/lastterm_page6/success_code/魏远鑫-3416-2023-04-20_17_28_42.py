TempStr = input()
if TempStr[0] in ['&'] :
    C = (eval(TempStr[1:]) )/6.78
    print("%.2f$"%(C))
elif TempStr[0] in ['R']: 
    C = (eval(TempStr[3:]) )/6.78
    print("%.2fUSD"%(C))
elif TempStr[0] in ['$'] :
    C = (eval(TempStr[1:]) )*6.78
    print("%.2f&"%(C))
elif TempStr[0] in ['U'] :
    C = (eval(TempStr[3:]) )*6.78
    print("%.2fRMB"%(C))
else:
    print("Error")
