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
ls1.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(ls1[0],ls1[1],ls1[2],ls1[3],ls1[4]))

