ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2 =ls*n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   a=ord(x)
   ls4.append(chr(a))

print(ls4)

