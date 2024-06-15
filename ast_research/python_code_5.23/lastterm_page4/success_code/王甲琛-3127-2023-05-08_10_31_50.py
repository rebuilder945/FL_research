n=int(input())
lst=[i for i in range(1,n+1)]
a=lst[0]
for i in range(n-1):
    lst[i]=lst[i+1]
lst[n-1]=a
print(lst)
