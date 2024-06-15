iMoneyStr=input()
if iMoneyStr[0] in ['$']:
    iCNY=eval(iMoneyStr[1:])*6.78
    print("&%.2f"%(iCNY))
elif iMoneyStr[0:3] in ['USD']:
    eCNY=eval(iMoneyStr[3:])*6.78
    print("RMB%.2f"%(eCNY))
elif iMoneyStr[0] in ['&']:
    iUSD=eval(iMoneyStr[1:])/6.78
    print("$%.2f"%(iUSD))
elif iMoneyStr[0:3] in ['RMB']:
    eUSD=eval(iMoneyStr[3:])/6.78
    print("USD%.2f"%(eUSD))
else:
    print("Error")

