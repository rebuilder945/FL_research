stu={}
lst=input().split(" ")
stu['name']=lst[0]
stu['english']=int(lst[1])
stu['python']=int(lst[2])
stu['math']=int(lst[3])
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
lst2=list(stu.items())
lst2[1:4].sort(key=lambda x:x[1],reverse=True)
print(lst2[0][1],end=' ')
for x in lst2[1:]:
    print('{:.2f}'.format(x[1]),end=" ")
