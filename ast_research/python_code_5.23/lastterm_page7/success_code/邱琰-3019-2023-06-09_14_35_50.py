n=list(input().split())
stu={}
stu['name']=n[0]
stu['english']=n[1]
stu['python']=n[2]
stu['math']=n[3]
stu=sorted(stu.items(),key=lambda x:x[1],reverse=True)
stu['avg']=(n[1]+n[2]+n[3])/3
ls=list(stu.keys())
print(''.join(ls))
