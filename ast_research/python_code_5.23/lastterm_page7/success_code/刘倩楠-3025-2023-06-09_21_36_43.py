num=input().split(" ")
a=[]
for x in num:
    a.append(x)
a.sort()
d={}
for i in a:
    d[i]=a.count(i)
lk=[]
lv=[]    
for k,v in d.items():
    lk.append(k)
    lv.append(int(v))
for x in list(range(len(lv))):
    if int(lv[x])==max(lv):
        print(lk[x],lv[x])
