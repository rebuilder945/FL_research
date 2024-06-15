name=map(str,input().split(","))
grade=map(int,input().split(","))
lst1=list(name)
lst2=list(grade)
lst4=[]
for i in range(len(lst1)):
    lst3=[lst1[i],lst2[i]]
    lst4.append(lst3)
lst4.sort(key=lambda x:x[1])
print(lst4)
