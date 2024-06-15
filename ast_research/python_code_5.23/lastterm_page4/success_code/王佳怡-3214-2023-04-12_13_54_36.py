l=list(eval(input()))
l1=l.copy()
l2=[]
for i in l:
    if i==0:
        l1.remove(i)
        l2.append(i)
l3=l1+l2
print(l3)
