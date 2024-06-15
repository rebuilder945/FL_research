ls = eval(input())
n = eval(input())
# 重复列表元素n次
for i in range(n):
     ls2=ls.append(ls[0])
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4=list(set(ls3))
   ls4.sort(key=ls3.index)

print(ls4)

