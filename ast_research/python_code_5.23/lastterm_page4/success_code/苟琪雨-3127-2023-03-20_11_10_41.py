n=eval(input())
list1=[i for i in range(1,n+1)]
a=list1[0]
for i in range(len(list1)-1):
    list1[i]=list1[i+1]
    list1[i+1]=a
print(list1)
