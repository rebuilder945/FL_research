#已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。要求，把姓名和对应的成绩进行组合，
#形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。最后输出形成的新列表。
#tom,jack,jone,mike
#[88,89,34,90]
Sname = input().split(',')
Sgrade = eval(input())
result = [[name, grade] for name, grade in zip(Sname, Sgrade)]
print(result)
