ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=n*ls
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
       ls5=ls3.copy
       a=ls5.pop(x)
       ls4=[a] 
       

print(ls4)

