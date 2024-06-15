n=eval(input())
lst=[x for x in range(1,n+1)]
lst2=[]
for i in range(1,n):
    lst2.append(lst[i])
lst2.append(lst[0])
print(lst2)
