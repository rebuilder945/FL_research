s = input()

if s[0] in ['$']:

    C = (eval(s[-1:0]))*6.78

    print("&%.2f"%(C))
elif s[0] in ['U']:

    C = (eval(s[3:]))*6.78

    print("RMB%.2f"%(C))


elif s[0] in ['&']:

    F = (eval(s[-1:0]) )/6.78

    print("$%.2f"%(F))
elif s[0] in ['R']:

    F = (eval(s[3:]) )/6.78

    print("USD%.2f"%(F))

else:

    print("Error")
