mostr=input()
if mostr[0]=="$":
    a=(eval(mostr[1:]))*6.78
    print("&%.2f"%a)
elif mostr[0]=="&":
    b=(eval(mostr[1:]))/6.78
    print("$%.2f"%b)
elif mostr[0:3]=="RMB":
    c=(eval(mostr[3:]))/6.78
    print("USD%.2f"%c)
elif mostr[0:3]=="USD":
    d=(eval(mostr[3:]))*6.78
    print("RMB%.2f"%d)
else:
    print("error")
