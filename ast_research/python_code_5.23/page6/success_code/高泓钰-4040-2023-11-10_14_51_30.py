w=input()
if w[0]in['&']:
    rmb=(eval(w[1:]))/6.78
    print("$%.2f"%rmb)
elif w[0]in["$"]:
    my=(eval(w[1:]))*6.78
    print("&%.2f"%my)
elif w[0:3]in['RMB']:
    my1=(eval(w[3:]))/6.78
    print("USB%.2f"%my1)
elif w[0:3]:
    qian=(eval(w[3:]))*6.78
    print("RMB%.2f"%qian)
else:
    print("Error")
