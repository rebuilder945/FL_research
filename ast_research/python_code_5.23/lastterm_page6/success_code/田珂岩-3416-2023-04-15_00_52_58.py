a = input()
if a[0] == "$":
    print("&%.2f"%(float(a[1:])*6.78))
elif a[0] == "&":
    print("$%.2f"%(float(a[1:])/6.78))
elif a[0:3] == "USD":
    print("RMB%.2f"%(float(a[3:])*6.78))
elif a[0:3] == "RMB":
    print("USD%.2f"%(float(a[3:])/6.78))
else:
    print("Error")        



