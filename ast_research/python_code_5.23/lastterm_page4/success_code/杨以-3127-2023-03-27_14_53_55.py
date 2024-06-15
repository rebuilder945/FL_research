n=eval(input())
list=[x for x in range(1,n+1)]
a=list[0]
for i in range(1,n):
    list[i-1]=list[i]
list[n-1]=a
print(list)

