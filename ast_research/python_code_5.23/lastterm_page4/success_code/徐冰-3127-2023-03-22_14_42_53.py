n=eval(input())
a=[x for x in range(1,n+1,1)]
b=[]
for i in range(0,n-1):
    b.append(a[i+1])
b.append(a[0])
print(b)

list1=[i for i in range(1,n+1)]
temp=list1[0]
for i in range(0,len(list1)-1):
    list1[i]=list1[i+1]
list[-1]=temp
print(list1)

