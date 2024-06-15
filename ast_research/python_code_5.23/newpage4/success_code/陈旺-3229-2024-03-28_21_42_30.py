a=list(input())
b=[]
a.remove("[")
a.remove("]")
c=((len(a)-1)/2)
for i in range(int(c)):
    a.remove(",")
for i in a:
    b.append(int(i))
h=[]
for i in b:
    n=b.count(i)
    if n==1:
        h.append(int(i))
    else:
        None
h.sort()
if h==[]:
    print(False)
else:
    print(",".join(map(str,h)))





