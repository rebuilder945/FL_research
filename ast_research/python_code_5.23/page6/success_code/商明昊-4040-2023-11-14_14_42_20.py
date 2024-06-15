n = input()
if n[0] in ["$"]:
    result = (eval(n[1:]))*6.78
    print("&%.2f"%result)
elif n[0] in ["&"]:
    result = (eval(n[1:]))/6.78
    print("$%.2f"%result)
elif n[0:3] in ["RMB"]:
    result = (eval(n[3:]))/6.78
    print("USD%.2f"%result)
elif n[0:3] in ["USD"]:
    result = (eval(n[3:]))*6.78
    print("RMB%.2f"%result)
else:
    print("Error")

