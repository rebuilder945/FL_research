a=input().split(',')
b=input().split(',')
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
d=list(c.items())
e=d.sort(key=lambda x:x[1],reverse=True)
for k,v in e:
    print(k,v,end=',')
