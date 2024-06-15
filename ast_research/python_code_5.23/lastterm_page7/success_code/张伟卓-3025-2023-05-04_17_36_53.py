a=input().split(" ")
d={}
for i in a:
    d[i]=a.count(i)
cishu=max(d.values())
ls=[]
for i in d:
    if d[i]==cishu:
        ls.append(i)
ls.sort()
for i in ls:
    print("{} {}" .format(i,cishu))
