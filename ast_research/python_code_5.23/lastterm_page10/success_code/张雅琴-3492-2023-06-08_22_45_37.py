a=input()
lst=[]
for i in a:
    lst.append(i)
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
b=0
lst2=[]
for i in lst1:
    if lst.count(i)==1:
        b+=1
        lst2.append(i)
if b==0:
    print('None')
else:
    print(lst2[0])
