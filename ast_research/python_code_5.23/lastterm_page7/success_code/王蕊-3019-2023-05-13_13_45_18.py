stu={}
a,b,c,d=map(str,input().split(""))
stu["name"]=a
stu["english"]=float(b)
stu["python"]=float(c)
stu["math"]=float(d)
avg=(float(b)+float(c)+float(d))/3
ls1=[]
ls1.append(stu["english"])
ls1.append(stu["python"])
ls1.append(stu["math"])
ls1.sort()
ls1.reverse()
ls1.insert(0,stu["name"])
la1.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst1[0],lst1[1],lst1[2],lst1[3],lst1[4]))

