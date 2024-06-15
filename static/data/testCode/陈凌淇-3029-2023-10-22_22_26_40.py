names = input().split(',')
scores = input().strip('[]').split(',')

# 转换成整数
scores = [int(score) for score in scores]

# 合并成嵌套列表
result = list(zip(names, scores))

# 输出结果
print(result)

