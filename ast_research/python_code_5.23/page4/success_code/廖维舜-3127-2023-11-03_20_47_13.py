n=eval(input())
list1=[x for x in range(1,n,1)]
list2=list1.copy()
for x in range(n-1):
    list2[x]=list1[x+1]
list2[n-1]=list1[0]
print(list2)
