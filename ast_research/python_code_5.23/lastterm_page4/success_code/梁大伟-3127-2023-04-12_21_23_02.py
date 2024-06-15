n=eval(input())
lst=[x for x in range(1,n+1)]
for i in range(len(lst)-1):
    if i<=len(lst)-2:
        lst[i]=lst[i+1]
lst[-1]=1
print(lst)

