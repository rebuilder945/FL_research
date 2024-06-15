ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=n*ls
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   times=ls3.count(x)
   if times>2
      while times>2
      ls3.remove(x)
      times-=1
    ls4=ls3.copy()

print(ls4)

