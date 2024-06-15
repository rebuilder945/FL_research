n=eval(input())
lst=[i for i in range(1,n+1)]
alst=lst.copy()
for x in range(0,n):
    if x>=1:
        lst[x]=lst[x-1]
    if x==0:
        lst[0]=lst[n-1]
print(lst)
