a=input()
if a[0] in ["&"]:
    us=(1/6.78)*eval((a[1:]))
    print("$%.2f"%us)
elif a[0] in ["$"]:
    cn=(6.78*eval(a[1:]))
    print("&%.2f"%cn)
elif a[0:3] in ["RMB"]:
    us=(1/6.78)*eval(a[3:])
    print("USD%.2f"%us)
elif a[0:3] in ["USD"]:
    cn=((6.78*eval(a[3:])))
    print("RMB%.2f"%cn)
else:
    print("Error")
