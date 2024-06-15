a=input()
b=input()
c=['red','blue','yellow']
if a not in c or b not in c:
    print('error')
if a==b:
    print('error')
else:
    if a=="red" and b=="blue":
        print('purple')
    if b=="red" and a=="blue":
        print('purple')
    if a=="red" and b=="yellow":
        print('orange')
    if b=="red" and a=="yellow":
        print('orange')
    if a=='blue' and b=="yellow":
        print('green')
    if b=='blue' and a=="yellow":
        print('green')
    
