ls = eval(input())
n = eval(input())

ls2 = []
for i in ls:
    ls1 = [i] * n  # 创建重复元素n次的列表
    ls2.extend(ls1)  # 将重复的列表添加到ls2中
#for 循环之后需要有一个缩进的代码块，否则会出现语法错误。
ls3 = [x*x for x in ls2]
ls4 = []
for x in ls3:
    if ls3.count(x) == 1:
        ls4.append(x)

print(ls4)