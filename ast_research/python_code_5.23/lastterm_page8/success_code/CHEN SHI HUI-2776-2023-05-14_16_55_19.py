def  myFun(a,b):
               if int(a)<=0 or int(b)<=0:
                       return "error"
               else:
                       a=int(a)
                       b=int(b)
                       i=0
                       while a>0 and b>0:
                               a1=a%10
                               b1=b%10
                               i+=a1*b1
                               a//=10
                               b//=10
                       return i


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

