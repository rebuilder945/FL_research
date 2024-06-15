name,english, python,math=(input().split( ))
stu={}
avg=(eval(english)+eval(python)+eval(math))/3
for x in [name, english,python,math,avg]:
    stu[x]=x
a=[eval(english),eval(python),eval(math)]
a.sort()
print(name,*a,"%.2f"%avg,sep=',')
