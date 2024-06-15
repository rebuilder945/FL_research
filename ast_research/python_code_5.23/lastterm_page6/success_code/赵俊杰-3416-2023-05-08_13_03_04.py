monstr=input()
if monstr[0]=="&":
    d=eval(monstr[1:])/6.78
    print("$%.2f"%(d))
elif monstr[0:3]=="RMB":
    d=eval(monstr[3:])/6.78
    print("USD%.2f"%(d))
elif monstr[0]=="$":
    r=eval(monstr[1:])*6.78
    print("&%.2f"%(r))
elif monstr[0:3]=="USD":
    r=eval(monstr[3:])*6.78
    print("RMB%.2f"%(r))
else:
    print(Error)

