moneyStr = input()

if moneyStr[0] == '$' or moneyStr[0:3] == 'USD':
    # 美元转人民币
    if moneyStr[0] == '$':
        money = eval(moneyStr[1:]) * 6.78
    else:
        money = eval(moneyStr[3:]) * 6.78
    print("&%.2f" % money)
elif moneyStr[0] == '&' or moneyStr[0:3] == 'RMB':
    # 人民币转美元
    if moneyStr[0] == '&':
        money = eval(moneyStr[1:]) / 6.78
    else:
        money = eval(moneyStr[3:]) / 6.78
    print("$%.2f" % money)
else:
    print("Error")

