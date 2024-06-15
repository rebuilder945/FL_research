TempStr = input()

if TempStr[0] in ["$"]:

    C = (eval(TempStr[1:]))*6.78

    print("&%.2f"%(C))
if TempStr[0:3] in ["USD"]:

    C = (eval(TempStr[3:]))*6.78

    print("%.2fRMB"%(C))

elif TempStr[0] in ["&"]:

    F = eval(TempStr[1:])/6.78

    print("$%.2f"%(F))
elif TempStr[0:3] in ["RMB"]:

    F = eval(TempStr[3:])/6.78

    print("USD%.2f"%(F))
else:

    print("Error")
