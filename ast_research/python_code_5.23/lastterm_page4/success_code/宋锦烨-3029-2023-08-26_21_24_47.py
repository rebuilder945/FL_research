 #已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。
 #要求，把姓名和对应的成绩进行组合，形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。最后输出形成的新列表。

names=input().split(',')
scores=eval(input())
result=[]
for i in names:
    toollist=[]
    toollist.append(i)
    a=names.index(i)
    b=scores[a]
    toollist.append(b)
    result.append(toollist)
print(result)
    
    

    
