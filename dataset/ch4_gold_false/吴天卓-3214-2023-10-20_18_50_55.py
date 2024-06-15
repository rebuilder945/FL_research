l=eval(input())
l1=[]
for i in l:
    if i !=0:
        l1.append(i)
        l.remove(i)
l1=l1+l
print(l1)

