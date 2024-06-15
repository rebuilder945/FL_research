a=input()
if a[0] in ["&"]:
    us=eval((1/6.78)*float(a[1:]))
    print("$%.2f"%us)
elif a[0] in ["$"]:
    cn=eval((6.78*float(a[1:])))
    print("&%.2f"%cn)
elif a[0:3] in ["RMB"]:
    us=eval((1/6.78)*float(a[3:]))
    print("'USD'%2f"%us)
elif a[0:3] in ["USD"]:
    cn=eval((6.78*float(a[3:])))
    print("RMB'%.2f"%cn)
else:
    print("Error")
