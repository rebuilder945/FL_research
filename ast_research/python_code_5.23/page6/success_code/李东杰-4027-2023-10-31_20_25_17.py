s=[]
e=[]
while True:
    a=input()
    s.append(a)
    if "#" in s:
        break
del s[-1]
n=len(s)
for x in s:
    b=int(x)
    e.append(b)
m=sum(e)
n=str(n)
m=str(m)

print(n," ",m)
