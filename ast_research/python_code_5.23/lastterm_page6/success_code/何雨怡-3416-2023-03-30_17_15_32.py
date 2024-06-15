money=input()
if money[0]=='$':
    RMB=eval(money[1:])*6.78
    print('&%.2f'%(RMB))
elif money[0:3]=='USD':
    rmb=eval(money[3:])*6.78
    print('RMB%.2f'%(rmb))
elif money[0]=='&':
    usd=eval(money[1:])/6.78
    print('$%.2f'%(usd))
elif money[0:3]=='RMB':
    USD=eval(money[3:])/6.78
    print('USD%.2f'%(USD))
else:
    print("Error")

