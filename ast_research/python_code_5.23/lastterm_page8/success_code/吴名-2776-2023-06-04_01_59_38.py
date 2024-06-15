def  myFun(a,b):
           if not a.isdigit() or not b.isdigit():
               return "error"
       
           if len(a) != len(b):
               return "error"
       
           result = 0
           for i in range(len(a)):
               result += int(a[i]) * int(b[i])
       
           return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

