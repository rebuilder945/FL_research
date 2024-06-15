ls = eval(input())
n = eval(input())
# 重复列表元素n次
l2=l1*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   	l3=list(set(l3))
   l4=l3

print(ls4)

