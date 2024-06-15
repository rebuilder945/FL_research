# 把姓名和成绩列表合并后按照成绩升序排列
# a=input().split(',')
# b=input().split(',')
# c=[]
# for i in range(0,len(a)):
#     c.append([a[i],int(b[i])])
# print(c)

def sort_scores(names, scores):
    # 将姓名和成绩配对起来，形成嵌套列表
    nested_list = [[name, int(score)] for name, score in zip(names, scores)]
    # 按照成绩升序排序
    sorted_list = sorted(nested_list, key=lambda x: x[1])
    return sorted_list

names = input().split(",")
scores = input().split(",")

result = sort_scores(names, scores)
print(result)
