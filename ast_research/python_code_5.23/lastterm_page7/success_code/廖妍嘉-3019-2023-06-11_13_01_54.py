m=input().split() 
stu=dict((('name',m[0]),('english',m[1]),('python',m[2]),('math',m[3])))
stu['avg']=(int(m[1])+int(m[2])+int(m[3]))/3
ls=[int(m[1]),int(m[2]),int(m[3])]
ls.sort(reverse=True)
print(m[0],'%s %s %s %s'%('%.2f'%(ls[0]),'%.2f'%(ls[1]),'%.2f'%(ls[2]),'%.2f'%(stu['avg'])))


