TempStr = input()

if TempStr[0] in ["&"]:

    C = (eval(TempStr[1]) *6.78)

    print("$%.2f"%(C))

elif TempStr[0] in ["$"]:

    F = eval(TempStr[1]/6.78)

    print("$%.2f"%(F))

else:

    print("Error")


