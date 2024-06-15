stu={}
a,b,c,d=map(str,input().split(''))
stu['name']=a
stu['english']=float(b)
stu['python']=float(c)
stu['math']=float(d)
avg=(float(b)+float(c)+float(d))/3
e=[]
e.append(stu['english'])
e.append(stu['python'])
e.append(stu['math'])
e.sort()
e.reverse()
e.insert(0,stu['name'])
e.insert(4,avg)
print(e[0],"%.2f", "%.2f","%.2f","%.2f"%(e[1],e[2],e[3],e[4]))

