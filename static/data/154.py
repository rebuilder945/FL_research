ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls5=list(set(ls3))
   ls5.sort(key=ls3.index)
   #在 for 循环内，ls5.sort(key=ls3.index) 这一行的缩进不正确
   ls4=ls5    


print(ls4)

