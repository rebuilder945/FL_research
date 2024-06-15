a=input()
if a[0] in ["$"]:
    b=6.78*eval(a[1:])
    print("&%.2f"%b)
elif a[0] in ["&"]:
    b=eval(a[1:])/6.78
    print("$%.2f"%b)
elif a[:3] in ["USD"]:
    b=6.78*eval(a[3:])
    print("RMB%.2f"%b)
elif a[:3] in ["RMB"]:
    b=eval(a[3:])/6.78
    print("USD%.2f"%b)
else:
    print("Error")

