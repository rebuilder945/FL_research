ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
       ls4=ls3.copy
       a=ls3.count(x)
       if a>1:
           for y in range(a-1):
               del ls4[ls4.index(x)]

print(ls4)

