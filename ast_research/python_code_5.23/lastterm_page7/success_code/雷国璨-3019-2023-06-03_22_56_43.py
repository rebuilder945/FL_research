stu={}
a,b,c,d=input().split(' ')
stu['name']=a
stu['english']=eval(b)
stu['python']=eval(c)
stu['math']=eval(d)
stu['avg']=(b+c+d)/3
lst=[]
lst.append(stu['name'])
lst.append(stu['english'])
lst.append(stu['math'])
lst.sort()
lst.reverse()
lst.insert(0,stu['name'])
lst.inster(-1,stu['avg'])
print("%s %.2f %.2f %.2f"%(lst[0],lst[1],lst[2],lst[3],lst[4]))
