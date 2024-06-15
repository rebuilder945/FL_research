names = input().split(',')  # 以逗号分隔输入的姓名并存入列表
scores = input().strip('[]').split(',')  # 去除方括号，然后以逗号分隔输入的成绩并存入列表
scores = [int(score) for score in scores]  # 将成绩转换为整数类型

result = [[name, score] for name, score in zip(names, scores)]  # 使用zip函数将姓名和成绩对应起来，并生成嵌套列表

print(result)  # 输出新的列表

