money=input()
if money[0]=='R':
    money=money*6.78
    print('USD%.2f'%money)
elif money[0]=='&':
    money=money*6.78
    print('$%.2f'%money)
elif money[0]=='U':
    money=money/6.78
    print('RMB%.2f'%money)
elif money[0]=='$':
    money=money/6.78
    print('&%.2f'%money)
else:
    print('Error')
