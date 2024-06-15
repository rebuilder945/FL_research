lst1=input().split(',')
lst2=input().split(',')
for i in range(len(lst2)):
    lst2[i]=int(lst2[i])
lst=[]
for i in range(len(lst1)):
    lst.append([lst1[i],lst2[i]])
lst.sort(key=lambda x:x[1])

print(lst)
