moneystr = input()
if moneystr[0] in ["&"]:
    dollar = (eval(moneystr[1:]))/6.78
    print("$""%.2f" % dollar)
elif moneystr[0] in ["$"]:
    yuan = eval(moneystr[1:])*6.78
    print("&""%.2f" % yuan)
elif moneystr[0:3] in ["RMB"]:
    dollar = (eval(moneystr[3:]))/6.78
    print("USD""%.2f" % dollar)
elif moneystr[0:3] in ["USD"]:
    yuan = eval(moneystr[3:])*6.78
    print("RMB""%.2f" % yuan)
else:
    print("Error")
    

    
