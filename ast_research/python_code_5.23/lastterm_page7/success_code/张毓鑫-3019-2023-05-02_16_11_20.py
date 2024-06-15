a={'name':0,'英语成绩':0,'python成绩':0,'数学成绩':0}
b=input()
c=b.split(' ')
a['name']=b[0]
a['英语成绩']=b[1]
a['python成绩']=b[2]
a['数学成绩']=b[3]
d=[b[1],b[2],b[3]]
d.sort(reverse=True)
d.insert(0,b[0])
for i in d:
    print(i,end=" ")
