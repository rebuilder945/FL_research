ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls=[];
for i in range(n):
    ls+=ls

ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if not x in ls:
               ls.append(x)

print(ls4)

