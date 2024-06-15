x1=input()
x2=input()
date=['red','blue','yellow']
if x1==x2 or x1 not in date or x2 not in date:
    print('error')
elif x1!='red' and x2!='red':
    print('green')
elif x1!='blue' and x2!='blue':
    print('orange')
else:
    print('purple')

