TempStr = input()
if TempStr[0] in ['&']:
    C=(eval(TempStr[1:]))/6.78
    print("$%.2f"%(C))
elif TempStr[0:3] in ['RMB']:
    F=eval(TempStr[3:])/6.78
    print("USD%.2f"%(F))
elif TempStr[0] in ['$']:
    E=6.78*eval(TempStr[1:])
    print("&%.2f"%(E))
elif TempStr[0:3] in ['USD']:
    G=6.78*eval(TempStr[3:])
    print("RMB%.2f"%(G))
else:
    print("Error")
