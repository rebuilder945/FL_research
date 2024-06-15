Money = input()
if Money[0] in ['$']:
    R = 6.78*(eval(Money[1:]))
    print("&%.2f"%(R))
elif Money[0] in ['U']:
    R = 6.78*(eval(Money[3:]))
    print("RMB%.2f"%(R))
elif Money[0] in ['&']:
    R = (eval(Money[1:]))/6.78
    print("$%.2f"%(R))
elif Money[0] in ['R']:
    R = (eval(Money[3:]))/6.78
    print("USD%.2f"%(R))
else:
    print("Error")
