ls = eval(input())
n = eval(input())
# 重复列表元素n次
for i in range(n):
    ls2+=ls
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a=ls3.count(x)
   while a>1:
       ls4=ls3.remove(x)

print(ls4)

