a,b,c,d=input().split()
stu={}
stulst=[]
stu["english"]=int(b)
stu["python"]=int(c)
stu["math"]=int(d)
for k,v in stu.items():
    stulst.append([k,v])
    stulst.sort(key=lambda x:x[1],reverse=True)
print(a,"%.2f"%stulst[0][1],"%.2f"%stulst[1][1],"%.2f"%stulst[2][1],"%.2f"%(int(b)+int(c)+int(d))/3)
