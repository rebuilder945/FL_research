a=input()
if a[0]=="$":
    z=eval(a[1:])
    z=z*6.78
    print("&"+"{:.2f}".format(z))
elif a[:4]=="USD":
     z=eval(a[4:])
     z=z*6.78
     print("RMB"+"{:.2f}".format(z))
elif a[0]=="&":
    z=eval(a[1:])
    z=z/6.78
    print("$"+"{:.2f}".format(z))
elif a[:4]=="RMB":
    z=eval(a[4:])
    z=z/6.78
    print("USD"+"{:.2f}".format(z))


