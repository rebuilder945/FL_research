n = input().split()
stu={}
stu["english"] = n[1]
stu["python"] = n[2]
stu["math"] = n[3]
studentList = []
for k,v in stu.items():
    studentList.append([k,v])
studentList.sort(key=lambda x:int(x[1]),reverse=True)
print(studentList)
studentList.append(["name",n[0]])    
stu["avg"]=(int(n[1])+int(n[2])+int(n[3]))/3
print("%s %.2f %.2f %.2f"%(studentList[3][1],int(studentList[0][1]),int(studentList[1][1]),int(studentList[2][1])),"%.2f"%(stu["avg"]))

