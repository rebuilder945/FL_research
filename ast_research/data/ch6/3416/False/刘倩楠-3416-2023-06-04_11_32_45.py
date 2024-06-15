MoneyStr=input()
if MoneyStr[0] in ['&']:
    USD=eval(MoneyStr[1:])/6.78
    print("$%.2f"%(USD))
elif MoneyStr[0:3] in ['RMB']:
    USD=eval(MoneyStr[3:])/6.78
    print("RMB%.2f"%(USD))
elif MoneyStr[0] in ['$']:
    RMB=eval(MoneyStr[1:])*6.78
    print("&%.2f"%(RMB))
elif MoneyStr[0:3] in ['USD']:
    RMB=eval(MoneyStr[3:])*6.78
    print("USD%.2f"%(RMB))
else:
    print("Error")
