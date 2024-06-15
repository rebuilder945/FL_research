CURRENCY = input()
if CURRENCY[0] in '$':
    R = eval(CURRENCY[1:])*6.78
    print("&"'%.2f' % R)
elif CURRENCY[0] in '&':
    U = eval(CURRENCY[1:])/6.78
    print("$"'%.2f' % U)
elif CURRENCY[:3] in 'USD':
    R = eval(CURRENCY[3:])*6.78
    print('RMB''%.2f' % R)
elif CURRENCY[:3] in 'RMB':
    U = eval(CURRENCY[3:])/6.78
    print("USD"'%.2f' % U)
else:
    print('Error')
