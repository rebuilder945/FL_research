ls = eval(input())
n = eval(input())
# 重复列表元素n次
c=[]
for x in ls:
     ls2=[x]*n
     c.extend(ls2)
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if ls.count(x)>1:
      ls.remove(x)
      ls4.extend(ls3)

print(ls4)

