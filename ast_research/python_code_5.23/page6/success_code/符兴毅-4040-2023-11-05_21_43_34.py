money = input()
if money[0] == '$':  # 美元转人民币
    num = float(money[1:])*6.78
    print("&%.2f"%num)
elif money[0] == 'U':
    num = float(money[3:])*6.78
    print("RMB%.2F"%num)
elif money[0] == "&":  # 人民币转美元
    num = float(money[1:])/6.78
    print("$%.2f"%num)
elif money[0] == 'U':
    num = float(money[3:])/6.78
    print("RMB%.2f"%num)
else:
    print('Error')
