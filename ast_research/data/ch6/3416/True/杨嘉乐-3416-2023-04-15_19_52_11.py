m=input()
if m[0:3] in ['RMB','USD']:
    n=(eval(m[3:]))
    if m[0:3] in ['RMB']:
        print("USD%.2f"%(n/6.78))
    elif m[0:3] in ['USD']:
        print("RMB%.2f"%(n*6.78))
elif m[0] in ['&','$']:
    n=(eval(m[1:]))
    if m[0] in ['&']:
        print("$%.2f"%(n/6.78))
    elif m[0] in ['$']:
        print("&%.2f"%(n*6.78))
else:
    print("Error")

