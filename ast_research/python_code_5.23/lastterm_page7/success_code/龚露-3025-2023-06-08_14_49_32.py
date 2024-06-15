d={}
ls=input().split()
ls2=[]
for x in ls:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    ls2.append([k,v])
ls2.sort(key=lambda x:x[1])
b=ls2[-1][1]
ls2.sort(key=lambda x:x[0])
for x in ls2:
    if x[1]==b:
        m,n=x
        print(m,n)

