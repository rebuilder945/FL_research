n=eval(input())
lst=[x for x in range(1,n+1)]
for x in range(n):
    if x==n-1:
        lst[x]=1
    else:
        lst[x]=lst[x+1]
print(lst)
