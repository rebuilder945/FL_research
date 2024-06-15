m=input().split()
stu={"name":"Zhang","english":80,"python":90,"math":100}
stu['name']=m[0]
stu['english']=m[1]
stu['python']=m[2]
stu['math']=m[3]
stu['avg']=(m[1]+m[2]+m[3])/3
ls2=[]
ls2.append(stu.get('english'))
ls2.append(stu.get("python"))
ls2.append(stu.get("math"))
ls2.sort(reverse=True)
print(stu.get('name'),'%.2f'%ls2(0),'%.2f'%ls2(1),'%.2f'%ls2(2),'%.2f'%stu.get('avg'))

