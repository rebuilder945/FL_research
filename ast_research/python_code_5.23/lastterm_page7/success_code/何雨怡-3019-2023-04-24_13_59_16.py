lst=input().split()
stu={}
stu['name']=lst[0]
stu['english']='%.2f'%int(lst[1])
stu['python']='%.2f'%int(lst[2])
stu['math']='%.2f'%int(lst[3])
average=(int(lst[1])+int(lst[2])+int(lst[3]))/3
stu1=sorted(stu.items(),key=lambda x:x[1],reverse=True)
stu1['avg']='%.2f'%average
print(stu1)
