TempStr = input()
if TempStr[0] in ['$','W']:
    C = eval(TempStr[1:])*6.78
    print("&%.2f"%(C))
elif TempStr[0] in ['U','WWW']:
    C = eval(TempStr[3:])*6.78
    print("RMB%.2f"%(C))

elif TempStr[0] in ['&','W']:
    F = eval(TempStr[1:])/6.78
    print("$%.2f"%(F))

elif TempStr[0] in ['R','WWW']:
    F = eval(TempStr[3:])/6.78
    print("USD%.2f"%(F))

else:
    print("Error")

