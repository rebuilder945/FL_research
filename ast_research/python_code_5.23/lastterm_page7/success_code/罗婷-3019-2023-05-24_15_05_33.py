name,*grades=input().split()
grades=list(map(int,grades))
stu={}
stu['name']=name
stu['english']=grades[0]
stu['pythin']=grades[1]
stu['math']=grades[2]
stu['avg']=sum(grades)/len(grades)
grades.sort(reverse=True)
print(stu['name'],end=' ')
for grade in grades:
    print("%.2f"%grade,end=' ')
print("%.2f"%stu['avg'])

