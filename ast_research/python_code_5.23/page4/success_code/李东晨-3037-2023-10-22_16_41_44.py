ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[val for val in ls for x in range(n)]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   while ls3.count(x):
       ls3.remove(x)

print(ls4)

