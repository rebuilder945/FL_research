ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=sorted(ls*n)
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   while x in ls3:
           ls3.remove(x)
       ls4.append(x)

print(ls4)

