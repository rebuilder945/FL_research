ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=n*ls
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if ls3[x] not in ls4:
           ls4.append(ls3[x]) 

print(ls4)

