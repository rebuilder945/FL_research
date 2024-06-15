n=eval(input())

lst=[x+1 for x in range(n)]
temp=lst[0]
for i in range(n-1):
    lst[i]=lst[i+1]
lst[n-1]=temp
print(lst)
