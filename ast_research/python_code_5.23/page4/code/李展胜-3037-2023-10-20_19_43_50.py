ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 = [n for n in ls for n in (0,n),n>0]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4 = list(set(ls3))

print(ls4)

