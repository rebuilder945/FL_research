ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[]
for i in range(len(ls)):
    for t in range(n):
        ls2.extend([ls[i]])
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   for  x  in  ls3:
       for t in range(ls3.count(x)-1):
           if ls3.count(x)-1<=0:
               break
           ls3.remove(x)
           ls4=ls3

print(ls4)

