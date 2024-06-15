s=input().split()
a=s[0]
b=int(s[1])
c=int(s[2])
d=int(s[3])
stu={}
stu["name"]=a
stu['english']=b
stu["python"]=c
stu["math"]=d
e="%.2f"%((b+c+d)/3)
stu["avg"]=e
lst=[]
lst.append("%.2f"%b)
lst.append("%.2f"%c)
lst.append('%.2f'%d)
lst.sort()
lst1=[str(a)]+lst+[c]
for i in lst1:
    print(i,end=" ")

