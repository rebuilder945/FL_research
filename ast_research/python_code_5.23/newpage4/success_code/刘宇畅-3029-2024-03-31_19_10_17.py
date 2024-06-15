# 输入
names = input().split(',')
# 输入tom，jack，jerry再输出names得到的是['tom', 'jack', 'jerry']
scores = eval(input())
# # 组合姓名和成绩
result = [[names[i], scores[i]] for i in range(len(names))]
# # 输出
print(result)



