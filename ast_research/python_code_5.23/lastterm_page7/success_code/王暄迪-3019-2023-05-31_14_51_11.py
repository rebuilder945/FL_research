stu={}
a,b,c,d=map(str,input().split())
stu['name']=a
stu['english']=float(b)
stu['python']=float(c)
stu['math']=float(d)
avg=(float(b)+float(c)+float(d))/3
lst1=[]
lst1.append(b)
lst1.append(c)
lst1.append(d)
lst1.sort()
lst1.reverse()
lst1.insert(0,a)
lst1.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst1[0],lst1[1],lst1[2],lst1[3],lst1[4]))
