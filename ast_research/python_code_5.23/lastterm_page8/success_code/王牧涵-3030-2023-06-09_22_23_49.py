name = input().split(",") # 将输入的字符串按照逗号分隔，转换成列表
score = input().split(",") # 同上

# 将两个列表合并成一个嵌套列表
pair = list(zip(name, score)) # 使用zip()函数将两个列表合并成一个嵌套列表

# 按照成绩升序排序
pair = sorted(pair, key=lambda x: int(x[1])) # 使用sorted()函数对嵌套列表按照第二个元素（成绩）升序排序

# 输出列表
print(pair) # 直接用print输出
