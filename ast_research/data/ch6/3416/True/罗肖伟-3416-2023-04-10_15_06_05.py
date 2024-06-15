money = input()

if money[0] in ['U']:
    a=money[3:]
    a=float(a)
    a*=6.78
    print("RMB%.2f"%(a))

elif money[0] in ['R']:
    a=money[3:]
    a=float(a)
    a/=6.78
    print("USD%.2f"%(a))
elif money[0] in ['$']:
    a=money[1:]
    a=float(a)
    a*=6.78
    print("&%.2f"%(a))
elif money[0] in ['&']:
    a=money[1:]
    a=float(a)
    a/=6.78
    print("$%.2f"%(a))
else:

    print("Error")
