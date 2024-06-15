smoney = input()
if smoney[0] == '&':
    smoney = eval(smoney[1:])/6.78
    print('$%.2f'% smoney)
elif smoney[0] == '$':
    smoney = eval(smoney[1:])*6.78
    print('&%.2f'% smoney)
elif smoney[0:3] == 'RMB':
     smoney = eval(smoney[3:])/6.78
     print('USD%.2f'% smoney)
elif smoney[0:3] == 'USD':
    smoney = eval(smoney[3:])*6.78
    print('RMB%.2f'% smoney)
else: 
    print('Error')

