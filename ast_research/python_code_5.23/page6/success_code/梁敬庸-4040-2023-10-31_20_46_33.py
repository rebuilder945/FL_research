moneyStr = input()

if moneyStr[0] in ['$']:
    do = (eval(moneyStr[1:]) )*6.78
    print("&%.2f"%do)
elif moneyStr[0:3] in ["USD"]:
    do = (eval(moneyStr[3:]) )*6.78
    print("RMB%.2f"%do)
elif moneyStr[0] in ['&']:
    y = eval(moneyStr[1:]) /6.78
    print("$%.2f"%y)
elif moneyStr[0:3] in ["RMB"]:
    y = eval(moneyStr[3:]) /6.78
    print("USD%.2f"%y)
else:
    print("Error")




