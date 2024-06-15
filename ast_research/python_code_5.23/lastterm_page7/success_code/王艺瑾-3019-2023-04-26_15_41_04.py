
stu={}
name,english,python,math=input().split()

stu['english']=int(english)
stu['python']=int(python)
stu['math']=int(math)
avg=(stu['english']+stu['python']+stu['math'])/3
scores=list(stu.values())

scores.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(name,int(scores[0]),int(scores[1]),int(scores[2]),avg))

    

            


