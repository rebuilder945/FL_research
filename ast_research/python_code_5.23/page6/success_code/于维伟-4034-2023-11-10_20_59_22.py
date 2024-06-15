p=['red','blue','yellow']
a=input()
b=input()
if a==p[0]:
    if b==p[1]:
        print('purple')
    elif b==p[2]:
        print('green')
    elif b==p[0]:
        print("error")
if a==p[1]:
    if b==p[2]:
        print('purple')
    elif b==p[1]:
        print('error')
if a==p[2]:
    if b==p[2]:
        print('error')


