a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
b=[0,1,2,3,4,5,6,7,8,9,10]
c=[1,0,'X',9,8,7,6,5,4,3,2]
d=input()
e=len(d)
f=0
if e!=18:
    print('Error')
else:
    for i in range(17):
        f+=a[i]*int(d[i])
    g=f%11
    
    h=b.index(g)
    if d[-1]!='X':
        if c[h]==int(d[-1]):
            print('Correct')
        else:
            print('Wrong')
    else:
        if c[h]==d[-1]:
            print('Correct')
        else:
            print('Wrong')

