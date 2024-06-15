n=input().split()
n2=n[1:]
n1=[]
for i in n2:
    n1.append(int(i))
stu=dict(name=n[0],english=n1[0],python=n1[1],math=n1[2])
stu['avg']=sum(n1)/3
m=stu.pop('name')
lst=[]
for k,v in stu.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=true)  
print('"%s","%.2f","%.2f","%.2f","%.2f"'%(m,lst[0][1],lst[1][1],lst[2][1],lst[3][1])) 

