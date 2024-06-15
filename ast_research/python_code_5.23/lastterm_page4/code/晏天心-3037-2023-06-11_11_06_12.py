ls = eval(input())
n = eval(input())
# 重复列表元素n次
ls2&#160;=&#160;ls * n
ls3 = [x*x for x in ls2]
# 下面代码去除重复元素
ls4=[]
for x in ls3:
   if&#160;x&#160;not&#160;in&#160;ls4:
   &#160;&#160;     &#160;ls4.append(x)

print(ls4)

