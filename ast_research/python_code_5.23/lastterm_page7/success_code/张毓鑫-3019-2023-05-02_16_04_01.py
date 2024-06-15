a={'name':0,'英语成绩':0,'python成绩':0,'数学成绩':0}
b=input()
c=b.split(' ')
a['name']=b[0]
a['英语成绩']=b[1]
a['python成绩']=b[2]
a['数学成绩']=b[3]
d=c[0]
del c[0]
c.sort(reverse=True)
c.insert(0,d)
for i in c:
    print(i.endswith(' '))
