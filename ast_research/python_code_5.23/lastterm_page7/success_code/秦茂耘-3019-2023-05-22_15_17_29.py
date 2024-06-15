stu={}
a,b,c,d=map(str,input().split(' '))
stu['name']=a
stu['english']=float(b)
stu['python']=float(c)
stu['math']=float(d)
avg=(float(b)+float(c)+float(d))/3
lst1=[]
lst1.append(stu['english'])
lst1.append(stu['python'])
lst1.append(stu['math'])
lst1.sort()
lst1.reverse()
lst1.insert(0,stu['name'])
lst1.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst1[0],lst1[1],lst1[2],lst1[3],lst1[4]))
