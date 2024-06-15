a=input().split(" ") or "ok"
d={}
while a!="ok":
    n,g=a[0],a[1]
    g=int(g)
    d[n]=g
    a=input().split(" ") or "ok"
k=list(d.keys())
k.sort()
print(k)
v=list(d.values())

v.sort()

print(v)
if 'India' in k:
    print("yes")
else:
    print("no")
print(sum(v))


