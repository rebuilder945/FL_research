lst1=map(eval,input().split(","))
lst2=map(eval,input().split(","))
lst3=[]
for x in len(lst1):
    lst3.append([])
for i in len(lst2):
    lst3[i].append([lst1[i],lst2[i]])
lst3.sort(key=lambda x:x[0])
print(lst3)
