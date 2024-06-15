scores=[]
stu={}
name,english,python,math=input().split()
stu['name']=name
stu['english']=int(english)
stu['python']=int(python)
stu['math']=int(math)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
scores.append(stu)

scores.sort(key = lambda x:x["avg"],reverse=True)
for stu in scores:
    print("%s,%.2f,%.2f,%.2f,%.2f"%(stu['name'],scores[0],scores[1],scores[2],stu['avg']))

    

            


