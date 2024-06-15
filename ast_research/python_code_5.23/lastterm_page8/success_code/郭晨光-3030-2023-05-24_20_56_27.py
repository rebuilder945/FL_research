# 读取输入的姓名和成绩
names = input().split(',')
scores = list(map(int, input().split(',')))

# 将姓名和成绩配对，形成一个嵌套列表
nested_list = list(zip(names, scores))

# 对嵌套列表按照成绩升序排序
nested_list.sort(key=lambda x: x[1])

# 输出排序后的嵌套列表
print(nested_list)
