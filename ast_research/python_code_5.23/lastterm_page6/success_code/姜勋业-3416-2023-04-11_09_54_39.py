a = input()
if a[0] in ['&']:
    C = float(a[1:])/6.78
    print("$%.2f"%(C))
elif a[0] in ['R']:
    C = float(a[3:])/6.78
    print("USD%.2f"%(C))
elif a[0] in ['$']:
    F = float(a[1:])*6.78
    print("&%.2f"%(F))
elif a[0] in ['U']:
    F = float(a[3:])*6.78
    print("RMB%.2f"%(F))
else:
    print("Error")
