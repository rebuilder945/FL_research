n=eval(input())
lst=[x for x in range(1,n+1)]
lst1=[]
for i in range(1,n):
    lst1.append(lst[i])
lst1.append(lst[0])
print(lst1)
