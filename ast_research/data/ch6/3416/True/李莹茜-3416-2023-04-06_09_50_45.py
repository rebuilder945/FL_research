#人民币与美元的转换+[a:b]类顺序+if，elif,else
MoneyStr=input()
if MoneyStr[0] in ["&"]:
    r1=eval(MoneyStr[1:])/6.78
    print("$%.2f"%(r1))
elif MoneyStr[0:3] in ["RMB"]:
    r2=eval(MoneyStr[3:])/6.78
    print("USD%.2f"%(r2))
elif MoneyStr[0] in ["$"]:
    d1=6.78*eval(MoneyStr[1:])
    print("&%.2f"%(d1))
elif MoneyStr[0:3] in ["USD"]:
    d2=6.78*eval(MoneyStr[3:])
    print("RMB%.2f"%(d2))
else:
    print("Error")
