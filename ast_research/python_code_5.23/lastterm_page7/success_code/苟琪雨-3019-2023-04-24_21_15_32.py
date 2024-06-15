stu={}
lis=input().split()
score=[int(lis[1]),int(lis[2]),int(lis[3])]
score=sorted(score,reverse=True)
stu['name']=lis[0]
stu['english']=int(lis[1])
stu['python']=int(lis[2])
stu['math']=int(lis[3])
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
result=[]
result.append(lis[0])
result=result+score
result.append(stu['avg'])
print("%s %.2f %.2f %.2f %.2f"%(result[0],result[1],result[2],result[3],result[4]))

