a=list(input())
b=[]
a.remove("[")
a.remove("]")
c=((len(a)-1)/2)
for i in range(int(c)):
    a.remove(",")
for i in a:
    b.append(int(i))
b.sort(reverse=True)
h=[]
for x in b:
    m=x*(10**((len(b)-b.index(x))-1))    
    h.append(int(m))
print(sum(h))

