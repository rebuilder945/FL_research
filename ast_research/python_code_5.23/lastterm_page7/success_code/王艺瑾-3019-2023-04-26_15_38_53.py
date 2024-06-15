
stu={}
name,english,python,math=input().split()

stu['english']=int(english)
stu['python']=int(python)
stu['math']=int(math)
avg=(stu['english']+stu['python']+stu['math'])/3
scores=list(stu.values())

scores.sort(reverse=True)
print("%s","%.2f","%.2f","%.2f","%.2f"%(name,scores[0],scores[1],scores[2],avg),)

    

            


