lst0=[]
lst1=[x for x in range(2,1000)]
lst=[  ]
for x in range(1,1000):
    for y in range(2,int(x**1/2)+1):
        if x %y==0:
            lst0.append(x)
for x in lst1:
    if x not in lst0:
        lst.append(x)
lstla=eval(input())
lst2=[]
for x in lstla:
    if x in lst:
        lst2.append(x)
print(lst2)
