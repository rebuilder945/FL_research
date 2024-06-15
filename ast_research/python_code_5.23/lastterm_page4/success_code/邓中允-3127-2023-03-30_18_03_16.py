n=eval(input())
list1=range(1,n+1)
list2=[]
m=list1[0]
for i in range(len(list1)-1):
    list2.append(list2[i+1])
list2.append(m)
print(list2)





