m=input()
if m[0:3]in['USD','RMB']:
    num = eval(m[3:])
    if m[0:3]=="RMB":
        a=num/6.78
        print("USD%.2f"%(a))
    else:
        r=num*6.78
        print("RMB%.2f"%(r))
elif m[0]in['$','&']:
    num = eval(m[1:])
    if m[0]=="$":
        r=num*6.78
        print("&%.2f"%(r))
    else:
        a=num/6.78
        print("$%.2f"%(a))
else:
    print("Error")

