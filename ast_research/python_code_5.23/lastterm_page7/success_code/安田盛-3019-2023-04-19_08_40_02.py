n=input().split()
stu={}
stu["english"]=int(n[1])
stu['python']=int(n[2])
stu["math"]=int(n[3])
sum=0
for i in stu.values():
    sum+=i
ave=sum/len(stu)
a=list(stu.items())
a.sort(key=lambda x:x[1],reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(n[0],a[0][1],a[1][1],a[2][1],ave))






