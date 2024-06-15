d={}
ls=[]
ls2=[]
while True:
    a=input()
    if a=='q':
        break
    ls.append(a)
for x in ls:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    ls2.append([k,v])
ls2.sort(key=lambda x:x[1])
m,n=ls2[-1]
print(m,n)

