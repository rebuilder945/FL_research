a=input() or "q"
d={}
while a!="q":
    if a in d:
        d[a]+=1
    else:
        d[a]=1
    a=input() or "q"
dd=sorted(d.items(),key=lambda x:x[-1])
l=list(dd)
print(l[-1][0],str(l[-1][1]))


