ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 =ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a=ls2.index(x)
   ls4=ls4.append(ls3[a])

print(ls4)

