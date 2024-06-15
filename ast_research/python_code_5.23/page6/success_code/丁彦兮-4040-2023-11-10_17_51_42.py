TempStr = input()

if TempStr[0]=="$":

    C = eval(TempStr[1:]) *6.78

    print("&%.2f"%(C))

elif TempStr[0]=="&":

    F = eval(TempStr[1:])/6.78

    print("$%.2f"%(F))
elif  TempStr[0]=="U":

    C = eval(TempStr[3:]) *6.78

    print("RMB%.2f"%(C))

elif TempStr[0]=="R":

    F = eval(TempStr[3:])/6.78

    print("USD%.2f"%(F))
else:

    print("Error")


