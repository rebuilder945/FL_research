scores=[]
for i in range(5):
    stu={}
    stu['name']=input('输入姓名')
    stu['english']=int(input('输入英语成绩'))
    stu['python']=int(input('输入python成绩'))
    stu['math']=int(input('输入数学成绩'))
    stu['avg']=(stu['english']+stu['python']+stu['math'])/3
    scores.append(stu)
scores.sort(key = lambda x:x["avg"],reverse =True)
for stu in scores:
    print(stu['name'],stu['english'],stu['python'],stu['math'],stu['avg'])

