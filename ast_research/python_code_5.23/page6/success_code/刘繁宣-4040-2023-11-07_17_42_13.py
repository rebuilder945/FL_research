MoneyStr = input()
if MoneyStr[0] in ['$']:
    R1=(eval(MoneyStr[1:10]))*6.78
    print("&%.2f"%(R1))
elif MoneyStr[0] in ['&']:
    U1=(eval(MoneyStr[1:10]))/6.78
    print("$%.2f"%(U1))
elif MoneyStr[0] in ['U']:
    R2=(eval(MoneyStr[3:10]))*6.78
    print("RMB%.2f"%(R2))
elif MoneyStr[0] in ['R']:
    U2=(eval(MoneyStr[3:10]))/6.78
    print("USD%.2f"%(U2))
else:
    print("Error")

