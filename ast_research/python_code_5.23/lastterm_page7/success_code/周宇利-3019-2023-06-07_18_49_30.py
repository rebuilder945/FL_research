stu={}
a,b,c,d=map(str,input().split())
stu['name']=a
stu['eglish']=float(b)
stu['python']=float(c)
stu['math']=float(d)
avg=(float(b)+float(c)+float(d))/3
list1=[]
list1.append(float(b))
list1.append(float(c))
list1.append(float(d))
list1.sort()
list1.reverse()
list1.insert(0,stu['name'])
list1.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(list1[0],list1[1],list1[2],list1[3],list1[4]))
