a=input()
if a[0:3]=="USD":
    b=eval(a[3::])
    c=round(b*6.78,2)
    print("RMB"+str(c))
elif a[0:3]=="RMB":
    b=eval(a[3::])
    c=round(b/6.78,2)
    print("USD"+str(c))
elif a[0]=="$":
    b=eval(a[1::])
    c=b*6.78
    print("&%.2f"%c)
elif a[0]=="&":
    b=eval(a[1::])
    c=round(b/6.78,2)
    print("$"+str(c))
else:
    print("Error")
