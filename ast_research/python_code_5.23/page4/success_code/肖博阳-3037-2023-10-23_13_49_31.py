ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[]
for i in ls:
    i=1
    while i<=n:
        ls2.append(i)
        i+=1

ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if ls3.count(x)>=2:
       ls3.remove(x)
   if len(ls3)==len(ls):
       ls4.extend(ls3)
   
      

print(ls4)

