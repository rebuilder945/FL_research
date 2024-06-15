# 已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。
# 要求，把姓名和对应的成绩进行组合，形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。
# # 最后输出形成的新列表。
# def list(iName,iGrand):
#     for i in range(iName,iGrand):
#         a=iName+iGrand
#         # print()

Name=input().split(",")
Grand=eval(input())
List=[]
for i in range (len(Name)):
    List.append([Name[i],Grand[i]])
print(List)
    
# a=list(Name,Grand) 
# print(a)
# list=[Name+Grand]
# print(a)
