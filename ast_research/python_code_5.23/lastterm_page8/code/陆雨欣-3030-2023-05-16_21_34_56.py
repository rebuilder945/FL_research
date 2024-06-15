list1=input().split(',')
list2=input().split(',')
l=len(list1)
list=[]
for i in range(l):
    list.append([list[i],int(list2[i])])
list.sort(key=lambda x:x[],reverse=False)
print(list)
