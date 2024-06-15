a=input()
b=list(a)
c=len(b)
if c==0:
    print('None')
else:
    for i in b:
        d=b.count(i)
        if d==1:
            print(i)
            break
        



