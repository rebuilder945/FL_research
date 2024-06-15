ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[x for x in ls for j in range(n)]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4=ls3.remove()
   ls4=set(ls4)
   ls4=list(ls4)

print(ls4)

