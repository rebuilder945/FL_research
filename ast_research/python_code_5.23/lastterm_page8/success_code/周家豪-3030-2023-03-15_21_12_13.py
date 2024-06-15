name=input().split(",")
scores=input().split(",")
lsttotal=[]
for x in range(len(name)):
    lst=[]
    lst.append(name[x])
    lst.append(scores[x])
    lsttotal.append(lst)
print(lsttotal)
