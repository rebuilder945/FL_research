ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[x for x in ls for i in range(n)]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   ls=eval(input())
   n=eval(input())
   ls2=[x for x in ls for i in range(n)]
   ls3=[x*x for x in ls2]
   ls4=[]
   for x in ls3:
       if x in ls4:
           continue
       else:
           ls4.append(x)
   print(ls4)

print(ls4)

