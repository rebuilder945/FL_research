exchange_rate = 6.78

money = input()

if money[0] == '&' or money[0] == '$':
    if money[0] == '&':
        amount = eval(money[1:])
        result = amount / exchange_rate
        print('$%.2f' % result)
    else:
        amount = eval(money[1:])
        result = amount * exchange_rate
        print('&%.2f' % result)
elif money[:3] == 'RMB':
    amount = eval(money[3:])
    result = amount / exchange_rate
    print('USD%.2f' % result)
elif money[:3] == 'USD':
    amount = eval(money[3:])
    result = amount * exchange_rate
    print('RMB%.2f' % result)
else:
    print('Error')
