def  myFun(a,b):
           sum=0
           if len(a)>=len(b):
               for i in range(1,len(b)+1):
                    sum+=eval(a[(-1)*i])*eval(b[(-1)*i])
           if len(a)<len(b):
               for i in range(1,len(a)+1):
                   sum+=eval(a[(-1)*i])*eval(b[(-1)*i])
           return sum


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

