scores=[]
stu={}
name,english,python,math=input()
stu['name']=name
stu['english']=int(english)
stu['python']=int(python)
stu['math']=int(math)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
scores.append(stu)
scores.sort(key = lambda x:x["avg"],reverse =True)
for stu in scores:
    print(stu['name'],stu['english'],stu['python'],stu['math'],stu['avg'])

    

            


