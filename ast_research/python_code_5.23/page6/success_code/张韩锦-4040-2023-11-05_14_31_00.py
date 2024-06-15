a=input()
if a[0]=="$":
    rmb=eval(a[1:])*6.78
    print("&%.2f"%rmb)
if a[0]=="U":
    rmb=eval(a[3:])*6.78
    print("USD%.2f"%rmb)
if a[0]=="&":
    usd=eval(a[1:])/6.78
    print("$%.2f"%usd)
if a[0]=="R":
    usd=eval(a[3:])/6.78
    print("RMB%.2f"%usd)
