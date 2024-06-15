l=eval(input())
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
if l1==[]:
    print(False)
else:
    l1.sort()
    print(l1)
