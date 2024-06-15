a,b,c,d=input().split()
stu={}
stu['name']=a
stu['english']=int(b)
stu['python']=int(c)
stu['math']=int(d)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
e=stu['avg']
m=[stu['english'],stu['python'],stu['math']]
x=sorted(m,reverse=True)
print(a,end=" ")
for i in x:
    print("%.2f"%i,end=" ")
print("%.2f"%e)

