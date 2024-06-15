TempStr = input()
if TempStr[1] in ['$']:
    C = (eval(TempStr[1:]) )*6.78

    print("&%.2f"%(C))

elif TempStr[1] in ['&']:

    F = eval(TempStr[1:])/6.78

    print("$%.2f"%(F))
elif TempStr[0:2] in ['USD']:

    F = eval(TempStr[3:])*6.78

    print("RMB%.2f"%(F))
elif TempStr[0:2] in ['RMB']:

    F = eval(TempStr[3:])/6.78

    print("USD%.2f"%(F))

else:

    print("Error")
