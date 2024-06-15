lst0=input().split(",")
lst1=input().split(",")
lst2=[]
for x in range(len(lst0)):
    lst2.append([lst0[x],int(lst1[x])])
lst2.sort(key=lambda x:x[1])
print(lst2)

