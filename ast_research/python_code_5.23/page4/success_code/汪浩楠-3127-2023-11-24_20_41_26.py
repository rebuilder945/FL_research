n=int(input())
lst=[x for x in range(1,n+1)]
a=lst[1]
for i in lst[::]:
    if i <len(lst):
        lst[i-1]=lst[i]
        lst[-1]=a
print(lst)

