n=eval(input())
lst=[x for x in range(1,n+1)]
lst1=[]
for i in range(1,n+1):
    lst1.insert(i-2,lst[i-1])
print(lst1)
