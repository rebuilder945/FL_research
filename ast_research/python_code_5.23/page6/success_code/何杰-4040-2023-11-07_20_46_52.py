q=input()
if q[0]=="$":
    r=float(q[1:])*6.78
    print("&%.2f"%(r))
elif q[0]=="&":
    r=float(q[1:])/6.78
    print("$%.2f"%(r))
elif q[:3]=="USD":
    r=float(q[3:])*6.78
    print("RMB%.2f"%(r))
elif q[:3]=="RMB":
    r=float(q[3:])/6.78
    print("USD%.2f"%(r))
else:
    print('error')
