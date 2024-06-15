ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a=ls3.count(x)
   if  a>1:
           while a>1:
               ls3.remove(x)
               a-=1
   for x in ls3:
       ls4.insert(0,x)
   ls4.reverse()

print(ls4)

