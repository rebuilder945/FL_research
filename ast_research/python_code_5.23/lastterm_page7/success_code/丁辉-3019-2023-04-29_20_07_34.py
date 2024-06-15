a,b,c,d=input()
stu={}
stulst=[]
stu["english"]=int(b)
stu["python"]=int(c)
stu["math"]=int(d)
stu["avg"]=(int(b)+int(c)+int(d))/3
for k,v in stu.items():
    stulst.append([k,v])
    stulst.sort(key=lambda x:x[1],reverse=True)
print(a,"%.2f"%stu[0][1],"%.2f"%stu[1][1],"%.2f"%stu[2][1],"%.2f"%stu[3][1])
