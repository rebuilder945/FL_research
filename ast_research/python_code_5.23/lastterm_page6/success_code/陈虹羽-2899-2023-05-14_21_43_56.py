n,m=input().split(' ')
n=eval(n) 
m=eval(m)
a=[]
t=''
if m-n<=2 or type(m)!=int or type(n)!=int or n<0 or m<0:
    print('illegal input')
elif n==0:
    for i in range(n+1,m):
        t+=str(i)
        e=t
        for x in range(n,m):
            if x!=i:
                t+=str(x)
                c=t
            else:
                continue
            for z in range(n,m):
                if z!=i and z!=x:
                    t+=str(z)
                    a.append(t)
                    t=c
                else:
                    continue
            t=e
        t=''
                
else:
    for i in range(n,m):
        t+=str(i)
        e=t
        for x in range(n,m):
            if x!=i:
                t+=str(x)
                c=t
            else:
                continue
            for z in range(n,m):
                if z!=i and z!=x:
                    t+=str(z)
                    a.append(t)
                    t=c
                else:
                    continue
            t=e
        t=''
a.sort()
print(' '.join(a))
