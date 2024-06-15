ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[]
for i in ls:
    for x in range(n):
        ls2.append(i)

ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a=ls3.count(x)
   if a==1:
       ls4.append(x)
   print(ls4)


print(ls4)

