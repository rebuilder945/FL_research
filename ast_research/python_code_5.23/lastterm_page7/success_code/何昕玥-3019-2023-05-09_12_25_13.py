n = int(input("输入学生数量:"))

lst = []

for i in range(n):

    name = input(f"第{i+1}个学生的name:")

    english = float(input(f"第{i+1}个学生的english课程的成绩:"))

    python = float(input(f"第{i+1}个学生的python课程的成绩:"))

    math = float(input(f"第{i+1}个学生的math课程的成绩:"))

    stu = {"name":name,"english":english,"python":python,"math":math}

    stu["avg"] = round((english+python+math)/3,1)

    lst.append(stu)

print(*lst,sep='\n')
lst.sort(key=lambda x: x['avg'], reverse=True)

for x in lst:

    print('姓名:',x['name'],'平均分:',x['avg'])
