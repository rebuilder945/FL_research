def  myFun(a,b):
       for i in range(n):
                       x='3'*(n-i-1)+'1'+'2'*i
                       l=' '.join(x)
                       print(l)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

