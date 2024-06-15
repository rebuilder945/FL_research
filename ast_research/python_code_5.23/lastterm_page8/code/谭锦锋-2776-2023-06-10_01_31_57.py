def  myFun(a,b):
       s=0
       a=int(a)
       b=int(b)
       whlie a!=0 and b!=0:
         a1=a%10
         b1=b%10
         s+=a1*b1
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

