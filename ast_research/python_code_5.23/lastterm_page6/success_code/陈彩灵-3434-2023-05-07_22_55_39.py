c1 = input()
c2 = input()
pj={'red','blue'}
oj={'red','yellow'}
gj={'yellow','blue'}
yj={'red','blue','yellow'}
if c1 in yj and c2 in yj and c1!=c2:
    sj={c1,c2}
    if sj==pj:
        print('purple')
    elif sj==oj:
        print('orange')
    else:
        print('green')
else:
    print('error')

