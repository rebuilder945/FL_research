money = input()

if money[0] in ['U']:
    rnm=float(eval(money[3:]))*6.78
    print("RMB%.2f"%(rnm))
elif money[0] in ['&']:
    rnm=float(eval(money[1:len(money)+1]))*6.78
    print("&%.2f"%(rnm))
elif money[0] in ['R']:
    usd=float(eval(money[3:]))/6.78
    print("USD%.2f"%(usd))
elif money[0] in ['$']:
    rnm=float(eval(money[1:len(money)+1]))/6.78
    print("$%.2f"%(rnm))
else:

    print("Error")
