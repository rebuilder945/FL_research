Money = input()

if Money[0] in ['U']:

    C = (eval(Money[3:]) )*6.78

    print("RMB%.2f"%(C))
elif Money[0] in ['$']:
    C = (eval(Money[1:]) )*6.78
    print("&%.2f"%(C))
elif Money[0] in ['R']:
    C = (eval(Money[3:]) )/6.78
    print("USD%.2f"%(C))
elif Money[0] in ['&']:
    C = (eval(Money[1:]) )/6.78
    print("$%.2f"%(C))
else :print("Error")

