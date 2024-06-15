ls=[]
while True:
    d=input().split(" ")
    if d!=["ok"]:
        ls.append(d)
    else:
        break
dic=dict(ls)
k=[]
v=[]
for m,n in dic.items():
    k.append(m)
    v.append(int(n))
k.sort()
v.sort()
print(k)
print(v)
if "India" not in k:
    print("no")
else:
    print("yes")
print(sum(v))
