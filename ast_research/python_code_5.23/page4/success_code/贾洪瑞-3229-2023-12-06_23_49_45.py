l=eval(input())
l1=[]
s=""
for i in l:
    if l.count(i)==1:
        l1.append(i)
if l1==[]:
    print(False)
else:
    l1.sort()
    for a in l1:
        s=s+str(a)+","
    s=s[:len(s)-1]
    print(s)

