n=int(input())
l=[i for i in range(1,n+1)]
temp=l[0]
for i in range(len(l)-1):
    l[i]=l[i+1]
    l[i+1]=temp
print(l)
