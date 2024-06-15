a=input()
if a[0]=="$":
    z=eval(a[1:])
    z=z*6.78
    print("&"+"{:.2f}".format(z))
elif a[:3]=="USD":
     z=eval(a[3:])
     z=z*6.78
     print("RMB"+"{:.2f}".format(z))
elif a[0]=="&":
    z=eval(a[1:])
    z=z/6.78
    print("$"+"{:.2f}".format(z))
elif a[:3]=="RMB":
    z=eval(a[3:])
    z=z/6.78
    print("USD"+"{:.2f}".format(z))


