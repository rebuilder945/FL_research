TempStr = input()
if TempStr[0]=="&":
    C = eval(TempStr[1:])/6.78
    print("$%.2f"%(C))
elif TempStr[0:3]=="RMB":
    F = eval(TempStr[3:])/6.78
    print("USD%.2f"%(F))
elif TempStr[0]=="$":
    A = eval(TempStr[1:])*6.78
    print("&%.2f"%(A))
elif TempStr[0:3]=="USD":
    B = eval(TempStr[3:])*6.78
    print("RMB%.2f"%(B))
else:
    print("Error")
