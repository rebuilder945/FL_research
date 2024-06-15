n=int(input())
lst1=[x for x in range(1,n+1)]
lst2=[]
for i in range(1,n):
    lst2.append(lst1[i])
lst2.append(lst1[0])
print(lst2)
