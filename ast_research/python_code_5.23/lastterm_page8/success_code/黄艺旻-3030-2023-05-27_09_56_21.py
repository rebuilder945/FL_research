a=input().split(',')
b=input().split(',')
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
d=list(c.items())
e=d.sort(key=lambda x:x[1],reverse=True)
for m in e:
    print(m,end=',')
