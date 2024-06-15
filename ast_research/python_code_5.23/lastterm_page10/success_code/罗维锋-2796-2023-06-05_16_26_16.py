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
    while True:
        e=""
        if len(c)==0:
            break
        for x in range(len(c)):
            e+=a[c[x]]
            if c[x]!=x[x+1]:
                c=c[x+1:]
                d.append(e)
                break
d=sorted(d)
print(d[-1])

