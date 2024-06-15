def  myFun(a,b):
           min=len(a)
           x = 0
           if len(a)>=len(b):
               min=len(b)
           for i in range(min-1):
               x = x+int(a[-1+i])*int(b[-1+i])
           return x
               

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

