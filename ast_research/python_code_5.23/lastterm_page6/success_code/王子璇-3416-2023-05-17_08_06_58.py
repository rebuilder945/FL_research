money=input()
if money[0]=='$':
    a=money*6.78
    print('&%.2f'%a)
elif money=='U':
    a=money*6.78
    print('RMB%.2f'%a)
elif money[0]=='&':
    a=money/6.78
    print('$%.2f'%a)
elif money[0]=='R':
    a=money[0]/6.78
    print('USD%.2f'%a)
else:
    print('Error')
