m = input()
if m[0]in['$']:
    B = (eval(m[1::1]))*6.78
    print("&%.2f"%(B))
elif m[0]in['&']:
    C = (eval(m[1::1]))/6.78
    print("$%.2f"%(C))
elif m[0:3]in['USD']:
    D = (eval(m[3::1]))*6.78
    print("RMB%.2f"%D)
elif m[0:3]in['RMB']:
    E = (eval(m[3::1]))/6.78
    print("USD%.2f"%E)
else:
    print("Error")
