n=input()
a=[]
while n!="q":
    a.append(n)
    n=input()
d={}
for i in a:
    d[i]=a.count(i)
lt=[]
ls=[]
for k,v in d.items():
    lt.append(k)
    ls.append(int(v))
for x in list(range(len(ls))):
    if int(ls[x])==max(ls):
        print(lt[x],ls[x])
