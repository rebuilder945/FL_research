a,b,c,d=eval(input())
stu={}
stulst=[]
stu["english"]=b
stu["python"]=c
stu["math"]=d
stu["avg"]=(b+c+d)/3
for k,v in stu.items():
    stulst.append([k,v])
    stulst.sort(key=lambda x:x[1],reverse=True)
print(a,"%.2f"%stu[0][1],"%.2f"%stu[1][1],"%.2f"%stu[2][1],"%.2f"%stu[3][1])
