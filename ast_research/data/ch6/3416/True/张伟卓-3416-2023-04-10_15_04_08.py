m=input()
if  m[:3] in ['RMB'] : 
    r = eval(m[3:])/6.78 
    print("USD%.2f"%(r))
elif m[:1] in ['&']:
    r = eval(m[1:])/6.78 
    print("$%.2f"%(r))
elif m[:1] in ['$'] :
    d = eval(m[1:] )*6.78
    print("&%.2f"%(d))
elif  m[:3] in ['USD']:
     d = eval(m[3:] )*6.78
     print("RMB%.2f"%(d))
else:
     print("Error")
