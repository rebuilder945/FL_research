q=eval(input())
if q[0]=="$":
    r=int(q[1:])*6.78
    print("&%.2f"%(r))
elif q[0]=="&":
    r=int(q[1:])/6.78
    print("$%.2f"%(r))
elif q[:3]=="USD":
    r=int(q[3:])*6.78
    print("RMB%.2f"%(r))
elif q[:3]=="RMB":
    r=int(q[3:])/6.78
    print("USD%.2f"%(r))
