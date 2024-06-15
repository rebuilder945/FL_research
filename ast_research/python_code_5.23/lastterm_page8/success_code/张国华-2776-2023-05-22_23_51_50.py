def  myFun(a,b):
               if int(a)<=0 or int(b)<=0:  #判断输入是否为正整数
                   return "error"
               else:
                   sum=0
                   for i in range(len(a)):
                       if i<len(b):
                           sum+=int(a[-1-i])*int(b[-1-i])
                       else:
                           sum+=int(a[-1-i])*0
                   return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

