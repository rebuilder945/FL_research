ls = eval(input())
n = eval(input())
# 重复列表元素n次
Is2=[x for i in range(n) for x in Is] 
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if x not in Ist4:
        Ist4.append(x)
       

print(ls4)

