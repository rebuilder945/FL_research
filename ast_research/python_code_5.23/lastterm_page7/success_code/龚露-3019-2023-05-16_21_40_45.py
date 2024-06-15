stu={}
ls1 = input().split()
stu["name"]=ls1[0]
stu["english"]=ls1[1]
stu["python"]=ls1[2]
stu["math"]=ls1[3]
a=(eval(ls1[1])+eval(ls1[2])+eval(ls1[3]))/3
m=eval(ls1[1])
n=eval(ls1[2])
q=eval(ls1[3])
h = ls1[0]
stu["avg"]=a
print("%s,%.2f,%.2f,%.2f,%.2f"%h,m,n,q,a)

