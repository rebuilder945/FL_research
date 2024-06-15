n=input().split()
stu=dict(name=n[0],english=n[1],python=n[2],math=n[3])
stu[avg]=sum(n[1:])/3
m=stu.pop(name)
lst=[]
for k,v in stu:
    lst.apppend([k,v])
lst.sort(key=lambda x:x[1])  
print("%s,%.2f,%.2f,%.2f,%.2f",%(m,lst[0][1],lst[1][1],lst[2][1],lst[3][1])) 

