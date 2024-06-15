def  myFun(a,b):
           a1=a[::-1]
           b1=b[::-1]
           sum=0
           if len(a1)>=len(b1):
               for i in range(len(b1)):
                   sum+=int(a1[i])*int(b1[i])
           else:
               for i in range(len(a1)):
                   sum+=int(a1[i])*int(b1[i])
           return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

