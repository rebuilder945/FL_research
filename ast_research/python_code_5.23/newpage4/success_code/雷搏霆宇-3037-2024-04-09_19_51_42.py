ls = eval(input())
n = eval(input())
# 重复列表元素n次



ls = list(ls)
ls2 = [x for s in ls for x in [s]*n]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if x not in ls4:
       ls4.append(x)


print(ls4)

