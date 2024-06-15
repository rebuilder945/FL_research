# 获取用户输入整数
num = int(input())

# 初始化水仙花数列表
result = []

# 判断小于等于该整数的所有自然数中是否存在水仙花数
for i in range(1, num+1):
    sum = 0
    n = len(str(i))
    for j in str(i):
        sum += int(j) ** n
    if sum == i:
        result.append(str(i))

# 输出结果
if len(result)>0:
    print("".join(result))
else:
    print("none")

