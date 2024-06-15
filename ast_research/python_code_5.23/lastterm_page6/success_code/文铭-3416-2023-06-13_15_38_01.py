a = input()
if a[0] in ['&']:
    S = (eval(a[1:]))/6.78
    print("$%.2f"%(S))
elif a[0] in ['R']:
    S = (eval(a[3:]))/6.78
    print("USD%.2f"%(S))
elif a[0] in ['$']:
    C = 6.78*(eval(a[1:]))
    print("&%.2f"%(C))
elif a[0] in ['U']:
    C = 6.78*(eval(a[3:]))
    print("RMB%.2f"%(C))
else:
    print("Error")

