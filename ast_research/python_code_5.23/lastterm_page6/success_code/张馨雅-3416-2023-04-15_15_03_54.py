m = input('')

if m[0] in ['$']:

    C = (eval(m[1:]) )*(6.78)

    print("&%.2f"%(C))

elif m[0:3] in ['USD']:

    C = (eval(m[3:]) )*(6.78)

    print("RMB%.2f"%(C))


elif m[0] in ['&','RMB']:

    F = (eval(m[1:]))/(6.78)

    print("$%.2f"%(F))

elif m [0:3] in ['RMB']:

    F = (eval(m[3:]))/(6.78)
    
    print("USD%.2f"%(F))

else:

    print("Error")

