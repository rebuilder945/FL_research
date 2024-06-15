n=eval(input())
list1=[x for x in range(0,n)]
temp=list1[0]
for i in range(0,len(list1)-1):
    list1[i]=list1[i+1]
list1[-1]=temp
print(list1)
