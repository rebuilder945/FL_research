TempStr = input()
if TempStr.startswith("&"):
    C = eval(TempStr[1:])
    d=C/6.78
    print("$%.2f"%(d))                                    
elif TempStr.startswith("RMB"):
    C = eval(TempStr[3:])
    d=C/6.78
    print("USD%.2f"%(d))

elif TempStr.startswith("$"):
    C = eval(TempStr[1:])
    d=C*6.78
    print("&%.2f"%(d))

elif TempStr.startswith("USD"):
    C = eval(TempStr[3:])
    d=C*6.78
    print("RMB%.2f"%(d))

else:
    print("Error")


