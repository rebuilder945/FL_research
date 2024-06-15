a=input()
b=input()
c=['red','blue','yellow']
if a or b not in c or a==b:
    print('error')
elif a==c[0] and b==c[1]:
    print('purple')
elif a==c[1] and b==c[0]:
    print('purple')
elif a==c[0] and b==c[2]:
    print('orange')
elif a==c[2] and b==c[0]:
    print('orange')
elif a==c[1] and b==c[2]:
    print('green')
elif a==c[2] and b==c[1]:
    print('green')
