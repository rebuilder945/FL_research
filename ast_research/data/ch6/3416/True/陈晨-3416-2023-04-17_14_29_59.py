TempStr = input()

if TempStr[0] in ['$']:

    C = (eval(TempStr[1:len(TempStr)+1])*6.78)

    print("&%.2f"%(C))

elif TempStr[0] in ['U']:

    C = (eval(TempStr[3:len(TempStr)+1])*6.78)

    print("RMB%.2f"%(C))
elif TempStr[0] in ['R']:

    C = (eval(TempStr[3:len(TempStr)+1])/6.78)

    print("USD%.2f"%(C))
elif TempStr[0] in ['&']:

    C = (eval(TempStr[1:len(TempStr)+1])/6.78)

    print("$%.2f"%(C))

else:

    print("Error")

