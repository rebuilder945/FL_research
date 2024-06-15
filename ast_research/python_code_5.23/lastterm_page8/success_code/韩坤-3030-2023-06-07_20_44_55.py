lst=input().split(",")
lst1=input().split(",")
a=[]
for i in range(0,len(lst1)):
    lst2=[]
    lst2.append(lst[i])
    lst2.append(int(lst1[i]))
    a.append(lst2)
a=sorted(a,key=lambda x:x[1],reverse=False)
print(a)
