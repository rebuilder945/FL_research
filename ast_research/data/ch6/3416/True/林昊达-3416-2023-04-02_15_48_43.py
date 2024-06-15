MoneyStr = input()

if MoneyStr[0] in ['&']:

    U = (eval(MoneyStr[1:])/6.78)

    print("$%.2f"%(U))

elif MoneyStr[0] in ['$']:

    R = 6.78*eval(MoneyStr[1:])

    print("&%.2f"%(R))

elif MoneyStr[0] in ['R']:

    U = (eval(MoneyStr[3:])/6.78)

    print("USD%.2f"%(U))
elif MoneyStr[0] in ['U']:

    R = 6.78*eval(MoneyStr[3:])

    print("RMB%.2f"%(R))
else:

    print("Error")
