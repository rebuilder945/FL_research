s=[]
while True:
    a=input()
    if a=="q":
        break
    s.append(a)
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=max(d.values())
for k,v in d.items():
    if v==m:
        print(k,v)
