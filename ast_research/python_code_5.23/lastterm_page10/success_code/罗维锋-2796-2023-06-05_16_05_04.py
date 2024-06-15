a=input()
b=list(range(10))
c=[]
d=[]
for x in range(len(a)):
    if a[x] in str(b):
        c.append(x)
if len(c)==0:
    print("No digits")
else:
    e=1
    while True:
        if e=="":
            break
        e=""
        for x in range(len(c)):
            e+=a[c[x]]
            if c[x]==c[x+1]:
                continue
            else:
                d.append(e)
                m=c[x:]
                c=m
                break
d=sorted(d)
print(d[-1])

