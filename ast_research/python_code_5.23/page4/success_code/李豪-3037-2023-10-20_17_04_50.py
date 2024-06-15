ls = eval(input())
n = eval(input())
# 重复列表元素n次
Is2=[]
for i in n:
    a=[i]*n
Is2.extend(a)
    
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if Is3.count(x)!=1:
       Is3.remove(x)
   Is4.extend(Is3)

print(ls4)

