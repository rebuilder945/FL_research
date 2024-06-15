n=eval(input())
lst0=lst.copy()
lst=[x for x in range(1,n+1)]
for i in lst[1:]:
    lst0.append(i)
lst0.append(lst[0]) 
print(lst0)   
