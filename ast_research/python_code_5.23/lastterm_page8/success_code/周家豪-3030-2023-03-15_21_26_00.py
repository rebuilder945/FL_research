name=input().split(",")
scores=input().split(",")
scores1=list(map(int,scores))
lsttotal=[]
for x in range(len(name)):
    lst=[]
    lst.append(name[x])
    lst.append(scores1[x])
    lsttotal.append(lst)
for i in range(len(scores1)):
    for j in range(len(scores1)):
        if lsttotal[i][1]<lsttotal[j][1]:
            lsttotal[i],lsttotal[j]=lsttotal[j],lsttotal[i]
print(lsttotal)
