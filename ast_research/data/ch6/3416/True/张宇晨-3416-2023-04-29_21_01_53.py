CurStr = input()
if CurStr[:1] in ['&','$']:
    if CurStr[:1] in ['&']:
        U=(eval(CurStr[1:]) )/6.78
        print("$%.2f"%(U))
    else:
        R=(eval(CurStr[1:]) )*6.78
        print("&%.2f"%(R))
elif CurStr[:3] in ['RMB','USD']:
    if CurStr[:3] in ['RMB']:
        U=(eval(CurStr[3:]) )/6.78
        print("USD%.2f"%(U))
    else:
        R=(eval(CurStr[3:]) )*6.78
        print("RMB%.2f"%(R))
else:
    print("Error")
