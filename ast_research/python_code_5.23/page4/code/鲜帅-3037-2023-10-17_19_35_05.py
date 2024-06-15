ls = eval(input())
n = eval(input())
# 重复列表元素n次
 ls2 = ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls4 = ls3.copy()
   a = ls3.count(x)
   if a >=2:
       for i in range(a-1):
           ls4.remove(x)

print(ls4)

