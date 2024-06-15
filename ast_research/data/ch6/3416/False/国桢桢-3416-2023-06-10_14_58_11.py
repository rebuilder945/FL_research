TempStr = input()

if TempStr[0]=="&":

    C = (eval(TempStr[1:]) )/6.78

    print("%.2f$"%(C))

elif TempStr[0]=="$":

    C = (eval(TempStr[1:]) )*6.78

    print("%.2f&"%(C))
elif TempStr[0]=="U":

    C = (eval(TempStr[3:]) )*6.78

    print("%.2fRMB"%(C))

elif TempStr[0]=="R":

    C = (eval(TempStr[3:]) )/6.78

    print("%.2fUSD"%(C))
else:

    print("Error")
