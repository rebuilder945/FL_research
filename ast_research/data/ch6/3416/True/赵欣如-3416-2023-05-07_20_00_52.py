TempStr = str(input())
if TempStr[0] =="$":
    C = float(TempStr[1:])*6.78
    print("&%.2f"%(C))
elif TempStr[0:3]=="USD":
    C= float(TempStr[3:])*6.78
    print("RMB%.2f"%(C))
elif TempStr[0]=="&":
    F=float(TempStr[1:])/6.78
    print("$%.2f"%(F))
elif TempStr[0:3]=="RMB":
    F=float(TempStr[3:])/6.78
    print("USD%.2f"%(F))
else:
    print("Error")


