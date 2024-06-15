def  myFun(a,b):
           if not (a.isdigit() and b.isdigit()): # 判断a,b是否都是数字
               return "error"
           
           sum_ = 0 # 初始化计数器
           
           for i in range(min(len(a), len(b))):
               sum_ += int(a[-(i+1)]) * int(b[-(i+1)])
           
           return sum_

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

