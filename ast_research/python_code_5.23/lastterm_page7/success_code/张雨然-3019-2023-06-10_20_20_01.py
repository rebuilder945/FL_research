i=input().split()
stu={}
stu['name']=i[0]
stu['english']='%.2f'%i[1]
stu['python']='%.2f'%i[2]
stu['math']='%.2f'%i[3]
avg='%.2f'%((float(i[1])+float(i[2])+float(i[3]))/3)
stu['avg']=avg
marks=[float(i[1]),float(i[2]),float(i[3])]
marks.sort(reverse=True)
print(stu['name'],end=' ')
for i in marks:
    print(i,end=' ')
print(avg)
