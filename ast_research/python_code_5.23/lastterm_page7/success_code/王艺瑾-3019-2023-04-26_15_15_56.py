scores=[]
stu={}
name,english,python,math=input().split()
stu['name']=name
stu['english']=int(english)
stu['python']=int(python)
stu['math']=int(math)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
scores.append(stu)
scores.sort(key = lambda x:x["avg"],reverse =True)
a,b,c,d,e=stu.values()
print("%s,%.2f,%.2f,%.2f,%.2f"%(a,int(b),int(c),int(d),int(e)))

    

            


