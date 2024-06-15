MoneyStr = input()
if MoneyStr[0] in ['&']:
    USD = eval(MoneyStr[1:]) / 6.78
    print("${:.2f}".format(USD))
elif MoneyStr[0:3] in ['RMB']:
    USD = eval(MoneyStr[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif MoneyStr[0] in ['$']:
    RMB = 6.78 * eval(MoneyStr[1:])
    print("&{:.2f}".format(RMB))
elif MoneyStr[0:3] in ['USD']:
    RMB = 6.78 * eval(MoneyStr[3:])
    print("RMB{:.2f}".format(RMB))
else:
    print("Error")
