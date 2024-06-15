ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 = ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls5 = ls3.copy()
   if ls5.count(x) ==1:
       ls4.append(x)
   elif ls5.count(x) >1:
       for i in range(ls3.count(x)-1):
           ls5.remove(x)

print(ls4)

