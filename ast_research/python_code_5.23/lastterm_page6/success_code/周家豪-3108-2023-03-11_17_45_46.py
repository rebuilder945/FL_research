lst1=eval(input())
lst2=[]
lst3=[]
lst4=[]

for str in lst1:
    for i in str:
        lst2.append(i)
    lst2.sort()
for i in lst2:
    if i not in lst3:
        lst3.append(i)
        a=lst2.count(i)
        lst4.append(a) 
for i in range(0,len(lst3)):
    print('%s,%d'%(lst3[i],lst4[i]))
