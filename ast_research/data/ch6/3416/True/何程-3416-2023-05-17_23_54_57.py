TempStr=input()
if TempStr[0] in ['$']:
    c=eval(TempStr[1:])*6.78
    print("&%.2f"%(c))
elif TempStr[:3] in ["USD"]:
    c=eval(TempStr[3:])*6.78
    print("RMB%.2f"%(c))
elif TempStr[0] in ["&"]:
    f=eval(TempStr[1:])/6.78
    print("$%.2f"%(f))
elif TempStr[:3] in ["RMB"]:
    f=eval(TempStr[3:])/6.78
    print("USD%.2f"%(f))
else:
    print("Error")
