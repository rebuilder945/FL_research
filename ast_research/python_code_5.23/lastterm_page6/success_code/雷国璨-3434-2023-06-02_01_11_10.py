a=input()
b=input()
if (a=='red' and b=='blue') or (a=='blue' and b=='red'):
    print('purple')
elif (a=='red' and b=='yellow') or (a=='yellow' and b=='red'):
    print('orange')
elif (a=='blue' and b=='yellow') or (a=='yellow' and b=='blue'):
    print('green')
else:
    print('error')

