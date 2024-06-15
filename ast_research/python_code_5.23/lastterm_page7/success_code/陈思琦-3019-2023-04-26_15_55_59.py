a,b,c,d=[x for x in input().split()]
stu={}
stu["english"]=stu.get("english","%.2f"%int(b))
stu["python"]=stu.get("python","%.2f"%int(c))
stu["math"]=stu.get("math","%.2f"%int(d))
sorted(stu.items(),key=lambda x:x[1],reverse=True)
for i in stu.keys():
    q=stu[i]
stu["name"]=stu.get("name",a)
e=(int(d)+int(b)+int(c))/3
stu["avg"]=stu.get("avg","%.2f"%int(e))
print(stu["name"],q,q,q,stu["avg"])
