stu={}
lst=input().split(" ")
stu['name']=lst[0]
stu['english']=int(lst[1])
stu['python']=int(lst[2])
stu['math']=int(lst[3])
lst1=list(stu.items())
lst2=lst1[1:]
lst2.sort(key=lambda x:x[1],reverse=True)
lst2.append(('avg',(stu['english']+stu['python']+stu['math'])/3))
print(lst1[0][1],end=' ')
for x in lst2:
    print('{:.2f}'.format(x[1]),end=" ")
