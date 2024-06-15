money=input()
if money[0]=='$':
    a=eval(money[1:])*6.78
    print('&%.2f'%a)
elif money[0]=='U':
    a=eval(money[3:])*6.78
    print('RMB%.2f'%a)
elif money[0]=='&':
    a=eval(money[1:])/6.78
    print('$%.2f'%a)
elif money[0]=='R':
    a=eval(money[3:])/6.78
    print('USD%.2f'%a)
else:
    print('Error')
