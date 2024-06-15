def  myFun(a,b):
               a=int(a)
               b=int(b)
               sum=0
               while a>0 and b>0:
                       d1=a%10
                       d2=b%10
                       sum+=d1*d2
                       a//=10
                       b//=10
               return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

