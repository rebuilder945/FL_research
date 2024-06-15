scores=[]
for i in range(5):
    stu={}
    stu['name']=input('')
    stu['english']=int(input(''))
    stu['python']=int(input(''))
    stu['math']=int(input(''))
    stu['avg']=(stu['english']+stu['python']+stu['math'])/3
 
    scores.append(stu)
 
 
scores.sort(key = lambda x:x["avg"],reverse =True)
for stu in scores:
    print(stu['name'],stu['english'],stu['python'],stu['math'],stu['avg'])
 
