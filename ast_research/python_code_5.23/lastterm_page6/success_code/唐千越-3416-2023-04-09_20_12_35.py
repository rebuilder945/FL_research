Money = input()

if Money[0] in ['R']:

    C = (eval(Money[3:]))/6.78

    print("USD%.2fC"%(C))

if Money[0] in ['&']:

    C = (eval(Money[1:]))/6.78

    print("$%.2fC"%(C))

if Money[0] in ['U']:

    F = 6.78*eval(Money[3:])

    print("RMB%.2fF"%(F))

elif Money[0] in ['$']:

    F = 6.78*eval(Money[1:])

    print("&%.2fF"%(F))


else:

    print("Error")
