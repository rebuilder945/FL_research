lst1=map(list,input().split(','))
lst2=map(list,input().split(','))
sunlst=[]
for x in range(len(lst1)):
    lst=[]
    lst.append(lst1[x])
    lst.append(lst2[x])
    sunlst.append(lst)
print(sunlst)

