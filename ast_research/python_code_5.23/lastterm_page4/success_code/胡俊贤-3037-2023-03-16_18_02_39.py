ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   n=ls3.count(x)
   if n>1:
       for i in range(n-1):
           ls3.remove(x)
       ls4.append(x)
   else:
       ls4.append(x)
       

print(ls4)

