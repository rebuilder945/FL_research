a=input()
b=input()
if a=='red' and b=='blue' or b=='red' and a=='blua':
    print('purple')
elif a=='red' and b=='yellow' or b=='red' and a=='yellow':
    print('orange')
elif a=='yellow' and b=='blue' or a=='blue' and b=='yellow':
    print('green')
else:
    print('error')
