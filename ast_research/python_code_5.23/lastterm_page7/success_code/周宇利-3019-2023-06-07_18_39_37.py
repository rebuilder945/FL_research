stu={}
a,b,c,d=map(str,input().split())
stu['name']=a
stu['eglish']=float(b)
stu['python']=float(c)
stu['math']=float(d)
avg=(float(a)+float(b)+float(c))/3
list1=[]
list1.append(b)
list1.append(c)
list1.append(d)
list1.append(avg)
list1.sort()
list1.insert(0,stu['name'])
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(list1[0],list1[1],list1[2],list1[3],list1[4]))
