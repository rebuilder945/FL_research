lst=[]
while True:
    a=input()    
    if a=='q':
        break
    lst.append(a)
lst1=list(set(lst))
a={}
for i in lst1:
    a[i]=lst.count(i)
lst2=list(a.items())
lst2.sort(key=lambda x:x[1])
print(lst2[-1][0],lst2[-1][1])
