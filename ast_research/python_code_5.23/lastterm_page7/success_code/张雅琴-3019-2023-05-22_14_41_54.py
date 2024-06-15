a,b,c,d=map(str,input().split(" "))
stu={"name":a,"english":float(b),"python":float(c),"math":float(d)}
e=(float(b)+float(c)+float(d))/3
stu["avg"]=float(e)
lst=[]
lst.append(float(b))
lst.append(float(c))
lst.append(float(d))
lst.sort()
lst.reverse()
lst1=[stu["name"]]+lst+[stu["avg"]]
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst1[0],lst1[1],lst1[2],lst1[3],lst1[4]))
