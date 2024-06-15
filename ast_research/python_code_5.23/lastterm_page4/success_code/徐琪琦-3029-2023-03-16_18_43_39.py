#已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。要求，把姓名和对应的成绩进行组合，形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。最后输出形成的新列表。
namelist1 = list(input().split(","))     #必须先把namelist1变成一个列表！！！！可以用split，但是list（）不可以，因为会用元组来进行包装
scorelist1 = eval(input())
newlist1 = []
for i in range(len(namelist1)):
    newlist1.append([namelist1[i],scorelist1[i]])       #形成嵌套列表的处理方法
print(newlist1)
