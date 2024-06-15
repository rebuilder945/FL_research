n=eval(input())
lst=[x for x in range(1,n+1)]
a=lst[0]
for i in range(0,len(lst)-1):
    lst[i]=lst[i+1]
lst[n-1]=a
print(lst)
