money=input()
if money[0] in ['&']:
    m=(eval(money[1:]))/6.78
    print('$%.2f'%m)
elif money[0:2]==['RMB']:
    m=(eval(money[3:]))/6.78
    print('USD%.2f'%m)
elif money[0] in ['$']:
    m=(eval(money[1:]))*6.78
    print('&%.2f'%m)
elif money[0:2]==['USD']:
    m=(eval(money[3:]))*6.78
    print('RMB%.2f'%m)
else:
    print('Error')
