ls1=input().split(",")
ls2=input().split(",")
l=len(ls1)
ls=[]
for i in range(l):
    ls.append([ls1[i],int(ls2[i])])
ls.sort(key=lambda x:x[1],reverse=False)
print(ls)


    
