def  myFun(a,b):
           a1=str(a)
           b1=str(b)
           if len(a1)>=len(b1):
               for i in range(len(a1)):
                   c=a1[-(i+1)]*b1[-(i+1)]
           else:
               for i in range(len(b1)):
                   c=a1[-(i+1)]*b1[-(i+1)]
           return(c)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

