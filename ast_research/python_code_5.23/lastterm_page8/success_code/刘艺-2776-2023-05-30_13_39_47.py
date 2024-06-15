def  myFun(a,b):
       m = int(a)
       k = int(b)
       if m > 0 and k > 0 and m % 1 ==0 and k % 1==0:
           n = 0
           if len(a) == len(b):
               for i in range(len(a)):
                   n = n + int(a[0])*int(b[0])
               return n
           if len(a) < len(b):
               for i in range(len(a)):
                   n = n + int(a[i])*int(b[i+1])
               return n
           if len(a) > len(b):
               for i in range(len(b)):
                   n = n + int(a[i+1])*int(b[i])
               return n
       else:
           return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

