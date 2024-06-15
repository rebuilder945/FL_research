a,b,c,d=input().split()
stu={}
stu["english"]=int(b)
stu["python"]=int(c)
stu["math"]=int(d)
lst=list(stu.items())
lst.sort(key=lambda x:x[1],revevrse=True)
stu["name"]=a
stu["avg"]=(int(b)+int(c)+int(d))/3
print(stu["name"],"%.2f"%lst[0][1],"%.2f"%lst[1][1],"%.2f"%lst[2][1],"%.2f"%stu["avg"])
