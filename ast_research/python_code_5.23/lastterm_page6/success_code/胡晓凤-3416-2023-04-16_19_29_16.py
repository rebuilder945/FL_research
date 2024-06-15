a=input()
if a[0] in ["&"]:
    us=eval((("$")+str((1/6.78)*float(a[1:]))))
    print("%.2f"%us)
elif a[0] in ["$"]:
    cn=eval((("&")+str(6.78*float(a[1:]))))
    print("%.2f"%cn)
elif a[0:3] in ["RMB"]:
    us=eval((("USD")+str((1/6.78)*float(a[1:]))))
    print(us)
elif a[0:3] in ["USD"]:
    cn=eval((("RMB")+str(6.78*float(a[1:]))))
    print(cn)
else:
    print("Error")
