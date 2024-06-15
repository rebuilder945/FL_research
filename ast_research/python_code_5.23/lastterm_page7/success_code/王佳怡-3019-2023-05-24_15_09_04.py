stu={}
stu['name'],stu['english'],stu['python'],stu['math']=input()
l=list(stu.items())
l.sort(key=lambda x:x[1],reverse=True)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
print(stu['name'],"%.2f","%.2f","%.2f","%.2f"%(l[0][1],l[1][1],l[2][1],stu['avg']))
