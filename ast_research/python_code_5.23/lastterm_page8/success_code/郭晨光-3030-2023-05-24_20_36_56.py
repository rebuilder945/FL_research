# 输入姓名和成绩
names = input().split(',')
scores = list(map(int, input().split(',')))

# 将姓名和成绩合并成一个嵌套列表
nested_list = list(zip(names, scores))

# 按照成绩升序排序
sorted_list = sorted(nested_list, key=lambda x: x[1])

# 输出嵌套列表
print(sorted_list)

