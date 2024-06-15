
list=list(range(1,100,1))
list0=[]
for i in list:
    for x in list:
        if i%x==0:
            list0.append(i)
for m in list0:
    if list0.count(m)==2:
        list0.remove(m)
        print(list0)
            

