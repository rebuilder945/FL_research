ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if ls3.count(x)>1:
       a=set(ls3)
   b=list(a)
   for y in range b:
        b.append(ls4)

print(ls4)

