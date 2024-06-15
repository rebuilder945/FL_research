c1=str(input())
c2=str(input())
if c1==c2:
    print('error')
elif c1 and c2 not in ('red','blue','yellow'):
    print('error')
else:
    if (c1=='red' and c2=='blue') or (c2=='red' and c1=='blue'):
        print('purple')
    elif (c1=='red' and c2=='yellow') or (c2=='red' and c1=='yellow'):
        print('orange')
    elif (c1=='blue' and c2=='yellow') or (c2=='blue' and c1=='yellow'):
        print('green')
