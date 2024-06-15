M=input()
if M[0]=='$':
    RMB=6.78*float(M[1:])
    print("&%.2f"%(RMB))
elif M[0]=="&":
    dollar=float(M[1:])/6.78
    print("$%.2f"%(dollar))
elif M[:3]=="RMB":
    dollar=float(M[3:])/6.78
    print("USD%.2f"%(dollar))
elif M[:3]=='USD':
    RMB=6.78*float(M[3:])
    print("RMB%.2f"%(RMB))
else:
    print("error")
