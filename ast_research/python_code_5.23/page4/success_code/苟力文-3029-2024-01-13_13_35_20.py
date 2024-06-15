# 输入姓名和成绩
name_str = input()
score_str = input()

# 将字符串转换为列表
name_list = name_str.split(',')
score_list = eval(score_str)

# 组合姓名和成绩
result = [list(item) for item in zip(name_list, score_list)]

# 输出结果
print(result)

