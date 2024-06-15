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
lst.append(b)
lst.append(c)
lst.append(d)
lst.sort(reverse=True)
for i in range(0,len(lst)):
    lst[i]="%.2f"%(lst[i])
lst1=[a]+lst+[e]
for i in lst1:
    print(i,end=" ")

