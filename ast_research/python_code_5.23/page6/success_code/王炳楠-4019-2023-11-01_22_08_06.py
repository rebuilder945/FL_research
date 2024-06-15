a=list(input())
c=[]
for i in a:
    n=int(i)
    t=(n+5)%10
    c.append(t)
l=len(c)
for e in range((l-1)//2+1):
    c[e],c[l-1-e]=c[l-1-e],c[e]
print(("").join(str(z) for z in c))



