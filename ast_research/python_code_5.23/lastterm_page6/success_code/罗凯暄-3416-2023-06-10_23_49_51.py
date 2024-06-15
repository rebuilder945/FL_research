money = input()

if money[0] == '&':
    # 人民币转美元
    rmb = eval(money[1:])
    usd = rmb / 6.78
    print('$%.2f' % usd)
elif money[0] == 'R':
    # 人民币转美元
    rmb = eval(money[3:])
    usd = rmb / 6.78
    print('USD%.2f' % usd)
elif money[0] == '$':
    # 美元转人民币
    usd = eval(money[1:])
    rmb = usd * 6.78
    print('&%.2f' % rmb)
elif money[:3] == 'USD':
    # 美元转人民币
    usd = eval(money[3:])
    rmb = usd * 6.78
    print('RMB%.2f' % rmb)
else:
    print('Error')

