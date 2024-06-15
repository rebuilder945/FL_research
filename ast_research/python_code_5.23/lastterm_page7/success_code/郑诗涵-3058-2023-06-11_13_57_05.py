a=input() or "q"
b={}
while a!="q":
    b[a]=b.get(a,0)+1
    a=input() or "q"
c=list(b.values())
zuida=max(c)
for x in b:
    if b[x]==zuida:
        print(x,zuida)
