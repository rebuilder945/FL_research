ls = eval(input())
n = eval(input())
# 重复列表元素n次
Is2 = Is*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   Is4.append(x)
   if Is4.count(x) > 1:
       Is4.remove(x)

print(ls4)

