ls1=input().split(",")
ls2=list(map(int,input().split(',')))
ls3=[]
for i in range(0,len(ls1)):
    ls=[ls1[i],ls2[i]]
    ls3.append(ls)
ls3.sort(key=lambda x:x[1],reverse=True)
print(ls3)
