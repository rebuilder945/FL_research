list2=input().split(" ")
lst={}
for i in list2:
    if i not in lst:
        lst[i]=1
    else:
        lst[i]+=1

list1=list(lst.items())
list1=sorted(list1,key=lambda x:x[1],reverse=True)
max=list1[0][1]
list1=sorted(list1,key=lambda x:x[0])
for i in range(len(list1)):
    if list1[i][1]==max:
        print(list1[i][0],list1[i][1])
    else:
        break    

