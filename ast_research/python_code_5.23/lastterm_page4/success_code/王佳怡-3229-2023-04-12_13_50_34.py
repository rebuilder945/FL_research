l=list(eval(input()))
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
if len(l1)!=0:
    l1.sort()
    print(','.join(str(x) for x in l1))
else:
    print("False")

