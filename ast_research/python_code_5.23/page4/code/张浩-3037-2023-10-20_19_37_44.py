ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[]
for i in ls:
    ls1=[i]*n
    ls2.extend(ls1)
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ifls3.count(x)>1:
       ls3.remove(x)
   ls4.extend(ls3)

print(ls4)

