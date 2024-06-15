moneystr = input()
if moneystr[0] in ["U","u"]:
    RMB = eval(moneystr[3:])*6.78 
    print("RMB%.2f"%(RMB))
elif moneystr[0] in ["R","r"]:
    USD = eval(moneystr[3:])/6.78
    print("USD%.2f"%(USD))
elif moneystr[0] in ["$"]:
    rmb = eval(moneystr[1:])*6.78
    print("&%.2f"%(rmb))
elif moneystr[0] in ["&"]:
    usd = eval(moneystr[1:])/6.78
    print("$%.2f"%(usd))
else:
    print("Error")
