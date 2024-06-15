ls = eval(input())
n = eval(input())
# 重复列表元素n次
lst2=[x for x in ls]*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if lst3.count(i)>1:
   lst3.remove(i)
   lst4=lst3
       

print(ls4)

