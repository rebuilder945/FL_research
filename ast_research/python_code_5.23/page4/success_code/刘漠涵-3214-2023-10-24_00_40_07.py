list0=eval(input())
l1=[]
l2=[]
for i in list0:
    if i != 0:
        l1.append(i)
    if i == 0:
        l2.append(i)
l3=l1+l2
print(l3)
