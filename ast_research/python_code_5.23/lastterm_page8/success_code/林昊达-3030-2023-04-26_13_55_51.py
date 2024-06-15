# 【问题描述】

# 已知一个列表存放学生姓名，另外一个列表存放学生成绩。把姓名和成绩配对后，形成一个嵌套列表，按照成绩升序输出列表。
# 【输入形式】

# 第一行输入姓名，每个姓名用逗号分隔。第二行输入成绩，按照逗号分隔。
# 【输出形式】

# 直接用print输出列表
# 【样例输入】

# tom,james,jack

# 89,34,78
# 【样例输出】

# [['james', 34], ['jack', 78], ['tom', 89]]

# 【样例说明】

# 直接输出嵌套列表，姓名和成绩组合在一起。

def combine(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append([list1[i],list2[i]])
    list3.sort(key=lambda x:x[1])
    return list3
ls1=input().split(',')
ls2=input().split(',')
for i in range(len(ls2)):
    ls2[i]=int(ls2[i])
print(combine(ls1,ls2))
