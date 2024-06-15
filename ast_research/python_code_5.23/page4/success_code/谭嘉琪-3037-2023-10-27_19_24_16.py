ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[]
for i in ls:
    for x in range(n-1):
        ls2.append(i)

ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4.append(x)
   a=ls3.count(x)
   for i in range(a):
       ls3.remove(x)


print(ls4)

