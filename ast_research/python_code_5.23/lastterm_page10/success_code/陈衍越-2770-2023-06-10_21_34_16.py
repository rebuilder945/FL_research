a=list(input())
b=list(input())
c=a.copy()
c.sort()
d=b.copy()
d.sort()
if a!=b:
    if c==d:
        print('True')
    elif c!=d:
        print('False')
else:
    print('False')

    
