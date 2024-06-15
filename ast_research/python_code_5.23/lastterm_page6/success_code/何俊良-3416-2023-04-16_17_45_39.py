def currency_conversion(currency):
    if currency[0] == '&':
        value = float(currency[1:])
        converted = value / 6.78
        return "$%.2f" % converted
    elif currency[:3] == 'RMB':
        value = float(currency[3:])
        converted = value * 6.78
        return "USD%.2f" % converted
    elif currency[0] == '$':
        value = float(currency[1:])
        converted = value * 6.78
        return "&%.2f" % converted
    elif currency[:3] == 'USD':
        value = float(currency[3:])
        converted = value / 6.78
        return "RMB%.2f" % converted
    else:
        return "Error"

currency = input().strip().upper()  # 全部转为大写字母进行比较
print(currency_conversion(currency))

