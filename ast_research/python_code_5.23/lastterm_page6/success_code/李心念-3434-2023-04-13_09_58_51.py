c1=input()
c2=input()
c = ['red','blue','yellow']
p = ['red','blue']
o = ['red','yellow']
g = ['blue','yellow']
if c1 == c2 or c1 not in c or c2 not in c:
    print('error')
else:
    if c1 in p and c2 in p:
        print('purple')
    elif c1 in o and c2 in o:
        print('orange')
    else:
        print('green')
