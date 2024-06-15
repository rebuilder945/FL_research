n=eval(input())
lst=[x for x in range(1,n+1)]
lst[n-1]=lst[0]
for x in range(n-1):
    lst[x]=lst[x+1]
print(lst)
