ls1=input().split(",")
ls2=input().split(",")
l=len(ls1)
d=[]
for i in range(l):
    d.append([ls1[i],int(ls2[i])])
d.sort(key=lambda x:x[1],reverse=False)
print(d)


