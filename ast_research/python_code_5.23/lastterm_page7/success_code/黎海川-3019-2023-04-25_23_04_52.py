scores=[]
for i in range(5):
    stu={}
    stu['name']=input()
    stu['english']=eval(input())
    stu['python']=eval(input())
    stu['math']=eval(input())
    stu['avg']=(stu['english']+stu['python']+stu['math'])/3
 
    scores.append(stu)
 
 
scores.sort(key = lambda x:x["avg"],reverse =True)
for stu in scores:
    print(stu['name'],stu['english'],stu['python'],stu['math'],stu['avg'])
 

