l=eval(input())
l1=[]
for i in l:
    if i !=0:
        l1.append(i)
a=l.count(0)
l1=l1+[0]*a
print(l1)

