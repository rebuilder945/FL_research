m = input()
if m[0]=='$':
    RMB=6.78*float(m[1:])
    print("&%.2f"%(RMB))
elif m[0]=='&':
    dollar = float(m[1:])/6.78
    print("$%.2f"%(dollar))
elif m[:3]=='RMB':
    dollar=float(m[3:])/6.78
    print("USD%.2f"%(dollar))
elif m[:3]=='USD':
    RMB=6.78*float(m[3:])
    print("RMB%.2f"%(RMB))
else:
    print("Error")
