n=eval(input())
lst=[x for x in range(1,n+1)]
for i in range(len(lst)-1):
    lst[i+1],lst[i]=lst[i],lst[i+1]
print(lst)

    





