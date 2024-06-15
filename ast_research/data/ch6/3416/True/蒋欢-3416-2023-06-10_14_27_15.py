def Change(n):
    if n[:3]=="RMB":
        m=n[3:]
        m=float(m)
        print("USD%.2f"%(m/6.78))
    elif n[0]=="&":
        m=n[1:]
        m=float(m)
        print("$%.2f"%(m/6.78))
    elif n[:3]=="USD":
        m=n[3:]
        m=float(m)
        print("RMB%.2f"%(m*6.78))
    elif n[0]=="$":
        m=float(n[1:])
        print("&%.2f"%(m*6.78))
    else:
        print('Error')
n=input()
Change(n)
