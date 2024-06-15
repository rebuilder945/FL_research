stu=dict.fromkeys(["name","english","python","math"],'NOTKNOWN')
ls=input().split( )
ls1=[]
for x in ls[1:4]:
    ls1.append(int(x))
avg=sum(ls1)/len(ls1)
ls1.sort()
print(ls[0],"%.2f %.2f %.2f %.2f"%(ls1[2],ls1[1],ls1[0],avg))

