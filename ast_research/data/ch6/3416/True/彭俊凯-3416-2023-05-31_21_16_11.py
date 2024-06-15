a=input()
if a[0]in['&']:
    M=(eval(a[1:])/6.78)
    print("$%.2f"%(M))
elif a[0]in['$']:
    C=(eval(a[1:])*6.78)
    print("&%.2f"%(C))
elif a[0:3]in['RMB']:
    M=(eval(a[3:])/6.78)
    print("USD%.2f"%(M))
elif a[0:3]in['USD']:
    C=(eval(a[3:])*6.78)
    print("RMB%.2f"%(C))
else:
    print("Error")

