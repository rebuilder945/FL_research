TempStr = input()
if TempStr[0]=='$':
    A = eval(TempStr[1:])*6.78
    print("&%.2f"%(A))
elif TempStr[0:3]=='USD':
    A = eval(TempStr[3:])*6.78
    print("RMB%.2f"%(A))
elif TempStr[0]=='&':
    B = eval(TempStr[1:])/6.78
    print("$%.2f"%(B))
elif TempStr[0:3]=='RMB':
    B = eval(TempStr[3:])/6.78
    print("USD%.2f"%(B))
else:
    print("Error")
