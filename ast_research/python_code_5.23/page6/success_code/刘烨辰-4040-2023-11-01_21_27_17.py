m = input()
if m[:1] in ["&"]:
    a = eval(m[1:])/6.78
    print("$%.2f"%a)
elif m[:1] in ["$"]:
    a = eval(m[1:])*6.78
    print("&%.2f"%a)
elif m[:3] in ["RMB"]:
    a = eval(m[3:])/6.78
    print("USD%.2f"%a)
elif m[:3] in ["USD"]:
    a = eval(m[3:])*6.78
    print("RMB%.2f"%a)
else:
    print("Error")
