ls = eval(input())
n = eval(input())
# 重复列表元素n次
lst2 = ls * n
ls3 = [x * x for x in lst2]
# 下面代码去除重复元素
ls4 = []
for x in ls3:
    if x not in ls4:
        #在 if 语句下方缺少了一个缩进的代码块。
        ls4.append(x)

print(ls4)