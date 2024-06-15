ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2=ls
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
          ls4.append[x]
   ls5=[]
   for i in range(i,len(ls4)):
         if ls4[i]==ls4[i-1]:
             ls5.append(i)
   ls5.sort(reverse=True)
   for x in ls5:
        del ls4[x]

print(ls4)

