a=input().split()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
dd=sorted(d.items(),key=lambda x:x[0])
dd1=dict(list(dd))
ddd=sorted(dd1.items(),key=lambda x:x[-1])
l=list(ddd)
for i in l:
    if i[1]==l[-1][1]:
        print(i[0],str(i[1]))
