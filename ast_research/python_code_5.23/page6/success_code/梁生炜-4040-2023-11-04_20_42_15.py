MoneyStr = input()
if MoneyStr[0] in ("$"):
    R1 = (eval(MoneyStr[1:]))*6.78
    print("&%.2f"%(R1))
elif MoneyStr[0] in ("U"):
    R2  = (eval(MoneyStr[3:]))*6.78
    print("RMB%.2f"%(R2))
elif MoneyStr[0] in ("&"):
    S1 = eval(MoneyStr[1:])/6.78
    print("$%.2f"%(S1))
elif MoneyStr[0] in ("R"):
    S2 = eval(MoneyStr[3:])/6.78
    print("USD%.2f"%(S2))
else:
    print("Error")
