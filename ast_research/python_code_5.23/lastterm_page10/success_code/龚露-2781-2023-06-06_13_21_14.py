ls1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ls2=[1,0,'X',9,8,7,6,5,4,3,2]
a=input()
d=[]
if len(a)!=18:
    print('Error')
else:
    for x in range(len(a)-1):
        c=ls1[x]*int(a[x])
        d.append(c)
    e=sum(d)
    f=e%11
    m=(12-e)%11
    if a[-1]==ls2[m]:
        print('Correct')
    else:
        print('Wrong')
