a=input()
if a[0] in ["$"]:
    n=eval(a[1::])*6.78
    print("&%.2f"%(n))
elif a[0] in ["%"]:
    n=eval(a[1::])/6.78
    print("$%.2f"%(n))
elif a[0:3:] in ["USD"]:
    n=eval(a[3::])*6.78
    print("RMB%.2f"%(n))
elif a[0:3:] in ["RMB"]:
    n=eval(a[3::])/6.78
    print("USD%.2f"%(n))
else:
    print("Error")
