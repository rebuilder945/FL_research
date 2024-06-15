ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls*2
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   for  x  in  ls3:
       if x not in ls4:
           ls4.append(x)
       elif x in ls4:
           pass

print(ls4)

