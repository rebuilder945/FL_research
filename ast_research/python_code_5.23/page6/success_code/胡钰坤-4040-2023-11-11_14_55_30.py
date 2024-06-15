MoneyStr = input()
if MoneyStr[0] in ['&']:
    C = (eval(MoneyStr[1:])/6.78)
    print("$%.2f"%(C))
elif MoneyStr[0] in ['$']:
    C = (eval(MoneyStr[1:])*6.78)
    print("&%.2f"%(C))
elif MoneyStr[0:3] in ['RMB']:
    C = (eval(MoneyStr[4:])/6.78)
    print("USD%.2f"%(C))
elif MoneyStr[0:3] in ['USD']:
    C = (eval(MoneyStr[4:])*6.78)
    print("RMB%.2f"%(C))
else:
    print("Error")

