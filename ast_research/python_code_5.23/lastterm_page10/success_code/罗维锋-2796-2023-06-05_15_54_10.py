a=input()
b=list(range(10))
c=[]
d=[]
for x in range(len(a)):
    if a[x] in b:
        c.append(x)
if len(c)==0:
    print("No digits")
else:
    while True:
        if e=="":
            break
        for x in range(len(c)):
            e=""+a[c[x]]
            if c[x]==c[x+1]:
                continue
            else:
                d.append(e)
                c=c[x:]
                break
d=sorted(d)
print(d[-1])

