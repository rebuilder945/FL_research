c1=input()
c2=input()

if (c1=='red' and c2=='blue') or (c1=='blue' and c2=='red'):
    print('purple')
elif (c1=='red' and c2=='yellow') or (c1=='yellow' and c2=='red'):
    print('orange')
elif (c1=='blue' and c2=='yellow') or (c1=='yellow' and c2=='blue'):
    print('green')
else:
    print('error')
