ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 = [ls*5]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4 = []
for x in ls3:
    if ls3.count(x) == 1:
        ##尝试在 if 语句中进行赋值，这是不允许的。
        #正确的做法是使用 == 进行相等性检查。
        ls4.append(x)

print(ls4)