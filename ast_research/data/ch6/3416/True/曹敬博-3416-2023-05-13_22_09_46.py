money = input()
if money[0] == '&':  
    rmb = eval(money[1:])
    usd = rmb / 6.78
    print('${:.2f}'.format(usd))
    
elif money[0] == '$': 
    usd = eval(money[1:])
    rmb = usd * 6.78
    print('&{:.2f}'.format(rmb))
    
elif money[:3] == 'RMB':  
    rmb = eval(money[3:])
    usd = rmb / 6.78
    print('USD{:.2f}'.format(usd))
    
elif money[:3] == 'USD':  
    usd = eval(money[3:])
    rmb = usd * 6.78
    print('RMB{:.2f}'.format(rmb))
    
else:
    print('Error')


