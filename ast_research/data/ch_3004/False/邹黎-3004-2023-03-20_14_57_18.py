list=eval(input())
list0=[]
list1=[]
for x in range(1,10000):
    for i in list:
        if i%x==0:
            list0.append(i)
for x in list0:
    if list0.count(x)==2:
        list1.append(x)
        list1.remove(x)
print(list1)



