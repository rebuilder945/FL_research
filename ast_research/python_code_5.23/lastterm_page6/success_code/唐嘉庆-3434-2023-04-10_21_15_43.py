a=input()
b=input()
c=['red','blue','yellow']
if a!=b and a in c and b in c:
    if a in ['red','blue'] and b in ['red','blue']:
        print('purple')
    if a in ['blue','yellow'] and b in ['blue','yellow']:
        print('green')
    if a in ['red','yellow'] and b in ['red','yellow']:
        print('orange')
else:
    print('error')
