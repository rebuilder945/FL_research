a=input()
if a[0] =='$':
    b=(eval(a[1:]))*6.78
    print("&%.2f"%(b))
elif a[0:3]==['U','S','D']:
    b=(eval(a[3:]))*6.78
    print("RMB%.2f"%(b))
elif a[0]=='&':
    b=(eval(a[1:]))/6.78
    print("&%.2f"%(b))
elif a[0:3]==['R','M','B']:
    b=(eval(a[3:]))/6.78
    print("RMB%.2f"%(b))
else:
    print("Error")
    

