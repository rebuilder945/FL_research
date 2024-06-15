ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 = ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a = ls3.pop(x)
   if a in ls3:
       ls3.remove(a)
   ls4.append(a)

print(ls4)

