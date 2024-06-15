ls1=input().split(",")
ls2=input().split(",")
for i in range(len(ls1)):
    d=[]
    d.append(ls1[i],int(ls2[i]))
d.sort(key=lambda x:x[1],reverse=False)
print(d)


