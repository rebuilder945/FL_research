a=input()
if a[0] in ["&"]:
    us=(("$")+str(((1/6.78)*float(a[1:]))))
    print("%.2f"%us)
elif a[0] in ["$"]:
    cn=eval((("&")+str((6.78*float(a[1:])))))
    print("%.2f"%cn)
elif a[0] in ["RMB"]:
    us=(("USD")+str((1/6.78)*float(a[1:])))
elif a[0] in ["USD"]:
    cn=(("RMB")+str(6.78*float(a[1:])))
else:
    print("Error")
