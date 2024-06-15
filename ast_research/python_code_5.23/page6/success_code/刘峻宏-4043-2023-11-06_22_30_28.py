import copy


a=eval(input())
b=[]

for i in range(len(a)):
    list1=(a[i][0::1])
    for j in range(len(list1)):
        b.append(list1[j])

d=[]

for i in range (len(b)):
    if not b[i] in d :
        d.append(b[i])
d.sort()

for i in range(len(d)):
    
    
    print("%s,%s"%(str(d[i]),str(b.count(d[i]))))
