def  myFun(a,b):
        Output = 0
           a, b = int(a), int(b)
           while a > 0 or b > 0:
               Output += (a % 10) * (b % 10)
               a = a // 10
               b = b // 10
           return Output
          

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

