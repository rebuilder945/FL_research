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
    s=str(l1)
    print(s[1:len(s)-1])

