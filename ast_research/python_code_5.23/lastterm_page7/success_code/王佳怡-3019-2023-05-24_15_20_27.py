stu={}
a=input()
a=a.split()
l=[int(a[1]),int(a[2]),int(a[3])]
l=sorted(l,reverse=True)
stu['name']=a[0]
stu['english']=int(a[1])
stu['python']=int(a[2])
stu['math']=int(a[3])
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
result = []
result.append(stu['name'])
result.append(l[0])
result.append(l[1])
result.append(l[2])
result.append(stu['avg'])
print("%s %.2f %.2f %.2f %.2f" % (result[0] ,result[1] , result[2]  ,result[3] , result[4] ))

