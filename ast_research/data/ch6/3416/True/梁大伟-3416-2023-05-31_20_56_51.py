money=input()
if money[0]=='$':
    m=money[1::]
    print('&%.2f'%(eval(m)*6.78))
elif money[0]=='&':
    n=money[1::]
    print('$%.2f'%(eval(n)/6.78))
elif money[0:3]=='USD':
    o=money[3::]
    print('RMB%.2f'%(eval(o)*6.78))
elif money[0:3]=='RMB':
    p=money[3::]
    print('USD%.2f'%(eval(p)/6.78))
else:
    print('Error')
