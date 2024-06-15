n=list(input().split())
stu={}
stu['name']=n[0]
stu['english']=int(n[1])
stu['python']=int(n[2])
stu['math']=int(n[3])
n1=[stu['english'],stu['python'],stu['math']]
n1.sort(reverse=True)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
print("%s %.2f %.2f %.2f %.2f"%(n[0],n1[0],n1[1],n1[2],stu['avg']))
