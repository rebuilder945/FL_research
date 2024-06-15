stu={}
ls1 = input().split()
stu["name"]=ls1[0]
stu["english"]=ls1[1]
stu["python"]=ls1[2]
stu["math"]=ls1[3]
a=(int(ls1[1])+int(ls1[2])+int(ls1[3]))/3
stu["avg"]=str(a)
ls = list(stu.values())
m = ' '.join(ls)
print(m)

