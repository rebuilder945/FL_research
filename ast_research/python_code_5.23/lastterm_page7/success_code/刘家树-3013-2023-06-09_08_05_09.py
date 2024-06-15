a=input().split(" ") or "ok"
d={}
while a!="ok":
    n,g=a[0],a[1]
    g=int(g)
    d[n]=g
    a=input().split()or "ok"
k=list(d.keys())
v=list(d.values())
k.sort(key=lambda x:x[0])
v.sort(key=lambda x:x[1])
print(k)
print(v)
if 'India' in k:
    print("yes")
else:
    print("no")
print(sum(v))


