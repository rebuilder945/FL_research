ls = eval(input())
n = eval(input())
# 重复列表元素n次

ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4=ls3
      ls4.append(int(x))
      ls4 = sorted(ls4)
      for i in range(len(ls4)):
       ls4[x]=str(ls4[x])

print(ls4)

