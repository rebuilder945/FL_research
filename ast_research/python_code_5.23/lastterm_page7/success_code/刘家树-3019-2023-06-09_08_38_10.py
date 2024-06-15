n,e,p,m=input().split()
e,p,m=int(e),int(p),int(m)
avg=(e+p+m)/3
avg=float('%.3f'%(avg))
e=float('%.3f'%(e))
p=float('%.3f'%(p))
m=float('%.3f'%(m))
print(e,p,m)
d={}
d["name"]=101
d["english"]=e
d["python"]=p
d["math"]=m
d["avg"]=-1
print(d)
l=sorted(d.items(),key=lambda x:x[-1],reverse=True)

l=dict(list(l))

l["name"]=n
l["avg"]=avg

l=list(l.items())

print(l[0][1],l[1][1],l[1][1],l[3][1],l[4][1])
