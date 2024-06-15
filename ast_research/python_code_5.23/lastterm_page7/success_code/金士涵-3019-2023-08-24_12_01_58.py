stu={}
n,e,p,m=eval(input())
stu["name"]=str(n)
stu["english"]=float(e)
stu["python"]=float(p)
stu["math"]=float(m)
avg=(float(e)+float(p)+float(m))/3
stu["avg"]=float(avg)
lst=[]
lst.append(stu['english'])
lst.append(stu['python'])
lst.append(stu['math'])
lst.sort()
lst.insert(0,stu["name"])
lst.insert(4,stu["avg"])
print ("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst[0],lst[1],lst[2],lst[3],lst[4]))

