x=input()
if x[0] in ['$']:
    r=(eval(x[1:]))*6.78
    print("&%.2f"%r)
elif x[0] in ['&']:
    s=(eval(x[1:]))/6.78
    print("$%.2f"%s)
elif x[:3] in ['USD']:
    r=(eval(x[3:]))*6.78
    print("RMB%.2f"%r)
elif x[:3] in ['RMB']:
    s=(eval(x[3:]))/6.78
    print("USB%.2f"%s)
else:
    print("Error")
