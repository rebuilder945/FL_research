base=input()
t=""
for i in base:
    a=(int(i)+5)%10
    t+=str(a)
k=list(t)
k.reverse()
l=""
for x in k:
    l+=x

print(l)
