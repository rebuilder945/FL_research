ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=[x*n for x in ls]
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   jishu=ls4.count(x1)
   if jishu>1:
       while jishu>1:
           ls4.remove(x1)
           jishu-=1

print(ls4)

