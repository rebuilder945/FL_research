Money=input()
if Money[0]=="$":
    RMB=6.78*float(Money[1:])
    print("&%2f"%(RMB))
elif Money[0]=="&":
    doller=float(Money[1:])/6.78
    print("$%.2f"%(doller))
elif Money[:3]=="RMB":
    doller=float(Money[3:])/6.78
    print("USD%.2f"%(doller))
elif Money[:3]=="USD":
    RMB=6.78*float(Money[3:])
    print("RMB%.2f"%(RMB))
else:
    print("Error")
