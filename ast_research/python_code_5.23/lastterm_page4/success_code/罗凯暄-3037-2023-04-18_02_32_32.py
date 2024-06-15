ls = eval(input())
n = eval(input())
# 重复列表元素n次
Is2 = Is*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if lst.count(x)<1:
        lst.append(x)

print(ls4)

