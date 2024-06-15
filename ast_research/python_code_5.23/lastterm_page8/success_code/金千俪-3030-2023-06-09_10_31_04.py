lst=input().split(",")
lst2=input().split(",")
lst3=[]
for i in range(len(lst)):
    lst3.append([lst[i],int(lst2[i])])
lst4=sorted(lst3,key=lambda x:x[1])
print(lst4)
