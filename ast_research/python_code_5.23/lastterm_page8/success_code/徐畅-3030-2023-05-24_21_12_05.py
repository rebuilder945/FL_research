lst1=list(map(str,input().split(',')))
lst2=list(map(int,input().split(',')))
sunlst=[]
sunlst2=[]
for x in range(len(lst1)):
    lst=[]
    lst.append(lst1[x])
    lst.append(lst2[x])
    sunlst.append(lst)
sunlst1=[sunlst[0][1],sunlst[1][1],sunlst[2][1]]
for x in range(len(sunlst)):
    if sunlst[x][1]==min(sunlst1):
        sunlst2.append(sunlst[x])
for x in range(len(sunlst)):
    if sunlst[x] not in sunlst2 and sunlst[x][1]!=max(sunlst1):
        sunlst2.append(sunlst[x])
for x in range(len(sunlst)):
    if sunlst[x][1]==max(sunlst):
        sunlst2.append(sunlst[x])



    
print(sunlst2)

