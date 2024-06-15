def currency_converter(input_str):
    if input_str[0] == '$':
        try:
            dollars = float(input_str[1:])
            rmb = dollars * 6.88  # 美元转人民币汇率，假设为6.88
            return 'RMB{:.2f}'.format(rmb)
        except ValueError:
            return 'Error'
    elif input_str[0] == '&':
        try:
            rmb = float(input_str[1:])
            dollars = rmb / 6.88  # 人民币转美元汇率，假设为6.88
            return '${:.2f}'.format(dollars)
        except ValueError:
            return 'Error'
    else:
        return 'Error'


