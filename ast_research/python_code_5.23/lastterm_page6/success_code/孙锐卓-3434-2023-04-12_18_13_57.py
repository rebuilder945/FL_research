a=input()
b=input()
c=['red','yellow','blue']
if a not in c:
    print('error')
elif b not in c:
    print('error')
if a==b:
    print('error')
else:
    if a=='red':
        if b=='yellow':
            print('orange')
        if b=='blue':
            print('purple')
    if a=='yellow':
        if b=='red':
            print('orange')
        if b=='blue':
            print('green')
    if a=='blue':
        if b=='red':
            print('purple')
        if b=='yellow':
            print('green')


