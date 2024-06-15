def  myFun(a,b):
           for x in range(len(a)):
               c=a[x]*b[x]
           return c  

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

