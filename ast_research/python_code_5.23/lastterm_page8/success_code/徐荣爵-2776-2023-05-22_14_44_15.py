def  myFun(a,b):
           if len(a) == len(b):
               t = 0
               for i in range(len(a)):
                   t += int(a[i])*int(b[i])
               return t
           elif len(a) < len(b):
               a = '0'* (len(b) - len(a)) + a
               t = 0
               for i in range(len(a)):
                   t += int(a[i])*int(b[i])
               return t
           else:
               b = '0'* ( - len(b) + len(a)) + b
               t = 0
               for i in range(len(a)):
                   t += int(a[i])*int(b[i])
               return t

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

