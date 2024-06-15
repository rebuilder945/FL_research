TempStr = input()

if TempStr[0] in ["&"]:

    C = (eval(TempStr[1]) *6.78)

    print("%.2fC"%(C))

elif TempStr[0] in ["$"]:

    F = 1.8*eval(TempStr[1]/6.78)

    print("%.2fF"%(F))

else:

    print("Error")


