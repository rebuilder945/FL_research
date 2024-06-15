n=eval(input())
lst=[x for x in range(1,n+1)]
lstcopy=lst.copy()
for i in range(n):
    lst[i-1]=lstcopy[i]
print(lst)
