TempStr = input()
if TempStr[0] in ["$"]:
    RMB = eval(TempStr[1:])*6.78
    print("&""%.2f"%RMB)
elif TempStr[0:3] in ["USD","usd"]:
    RMB = eval(TempStr[3:])*6.78
    print("RMB""%.2f"%RMB)
elif TempStr[0:3] in ["RMB","rmb"]:
    RMB = eval(TempStr[3:])/6.78
    print("USD""%.2f"%RMB)
elif TempStr[0] in ["&"]:
    USD = eval(TempStr[1:])/6.78
    print("$""%.2f"%USD)
else:
    print("Error")
