n=eval(input())
list1=[x for x in range(1,n+1)]
list2=[]
list2+=list1[0]
for i in range(1,len(list1)):
    list2+=list1[i]
print(list2)


