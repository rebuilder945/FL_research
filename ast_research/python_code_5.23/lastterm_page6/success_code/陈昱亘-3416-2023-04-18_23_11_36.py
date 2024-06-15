money=input()
if money[0]=='$':
    yuan=6.78*eval(money[1:])
    print('&%.2f'%(yuan))
elif money[0]=='&':
    dollar=eval(money[1:])/6.78
    print('$%.2f'%(dollar))
elif money[0:3]=='USD':
    yuan=6.78*eval(money[3:])
    print('&%.2f'%(yuan))
elif money[0:3]=='RMB':
    dollar=eval(money[3:])/6.78
    print('$%.2f'%(dollar))
else: print('Error')
