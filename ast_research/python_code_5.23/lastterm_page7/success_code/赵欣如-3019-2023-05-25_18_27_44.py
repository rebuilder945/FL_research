ls=input().split()
stu={}
stu["name"]=str(ls[0])
stu["english"]=int(ls[1])
stu["python"]=int(ls[2])
stu["math"]=int(ls[3])
a=ls.pop(0)
for i in ls:
    ls[ls.index(i)]=int(i)
ls.sort(reverse=True)
ls.append(int(sum(ls)/3))
for x in ls:
    ls[ls.index(x)]='%.2f'%int(x)
print(a," ".join(str(x)for x in ls))

