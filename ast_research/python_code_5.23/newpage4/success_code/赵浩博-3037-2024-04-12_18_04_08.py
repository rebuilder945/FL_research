ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   for i in range(len(ls3)):
       if ls3[i:].count(ls3[i])==1:
        ls4.append(ls3[i])

print(ls4)

