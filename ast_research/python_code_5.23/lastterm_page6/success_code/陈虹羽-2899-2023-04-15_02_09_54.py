a=input().split(' ')
d=int(a[0])
e=int(a[-1])
b=[]
c=''
if d>=e or d<0 or d==e or e-d<=2 or e>=10 or d>=10:
    print('illegal input')
else:
    for i in range(d,e):
        c+=str(i)
        g=c
        for i in range(d,e):
            c+=str(i)
            f=c
            for i in range(d,e):
                c+=str(i)
                b.append(c)
                c=f
            c=g
        c=''
        
    print(b)



