m = input()
if m[0]in['&']:
    r = (eval(m[1::1]))/6.78
    print("$%.2f"%r)
elif m[0]in['$']:
    u =(eval(m[1::1]))*6.78
    print("&%.2f"%u)
elif m[0:3]in['USD']:
    u =(eval(m[3::1]))*6.78
    print("RMB%.2f"%u)
elif m[0:3]in['RMB']:
    R = (eval(m[3::1]))/6.78
    print("USD%.2f"%R)
else:
    print("Error")

