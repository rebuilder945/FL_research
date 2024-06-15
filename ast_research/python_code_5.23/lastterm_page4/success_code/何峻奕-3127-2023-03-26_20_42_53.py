n=eval(input())
lst=[i for i in range(1,n+1)]
alst=lst.copy()
for i in alst:
    if i>=1:
        lst[i]=lst[i-1]
    if i==0:
        lst[0]=lst[n-1]
print(lst)
