n=eval(input())
lst=[i for i in range(1,n+1)]
for x in range(0,n-1):
    lst[x]=lst[x+1]
lst[n-1]=1
print(lst)
