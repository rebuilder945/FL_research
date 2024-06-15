lst1=list(map(str,input().split(',')))
lst2=list(map(int,input().split(',')))
sunlst=[]
for x in range(len(lst1)):
    lst=[]
    lst.append(lst1[x])
    lst.append(lst2[x])
    sunlst.append(lst)
    lst.sort()
print(sunlst)

