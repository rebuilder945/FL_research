def  myFun(a,b):
       
           if b>a:
               a,b=b,a
           a=int(a)
           b=int(b)
           s=0
           while a>0 and b>0:
               m=a%10
               n=b%10
               s+=m*n
               a=a//10
               b=b//10
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

