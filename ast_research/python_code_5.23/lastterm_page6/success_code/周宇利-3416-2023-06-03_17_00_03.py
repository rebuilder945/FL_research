Moneystr=input()
if Moneystr[0] in ["$"]:
    a=eval(Moneystr[1:len(Moneystr)])*6.78
    print("&%.2f"%(a))
elif Moneystr[0] in ["&"]:
    b=eval(Moneystr[1:len(Moneystr)])/6.78
    print("$%.2f"%(b))
elif Moneystr[0:3] in["USD"]:
    c=eval(Moneystr[3:len(Moneystr)])*6.78
    print("RMB%.2f"%(c))
elif Moneystr[0:3] in ["RMB"]:
    d=eval(Moneystr[1:len(Moneystr)])/6.78
    print("USD%.2f"%(d))
else:
    print("Error")
