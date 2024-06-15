m = input()
if m[0]=="$":
    M = 6.78*eval(m[1:])
    print("&%.2f"%(M))
elif m[0]=="&":
    M = eval(m[1:])/6.78
    print("&%.2f"%(M))    
if m[0:2]=="USD":
    M = 6.78*eval(m[3:])
    print("RMB%.2f"%(M))
if m[0]=="RMB":
    M = eval(m[3:])/6.78
    print("&%.2f"%(M))
