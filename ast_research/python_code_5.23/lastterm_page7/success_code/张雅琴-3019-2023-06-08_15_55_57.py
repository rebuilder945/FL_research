a,b,c,d=eval(input())
stu={}
stu["name"]=str(a)
stu['english']=b
stu["python"]=c
stu["math"]=d
c="%.2f"%((b+c+d)/3)
stu["avg"]=c
lst=["%.2f"%b,"%.2f"%c,"%.2f"%d]
lst1=[str(a)]+lst+[c]
for i in lst1:
    print(i,end=" ")

