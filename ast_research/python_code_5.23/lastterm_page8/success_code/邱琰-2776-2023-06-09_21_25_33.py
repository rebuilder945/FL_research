def  myFun(a,b):
       s=0
       a=int(a)
       b=int(b)
       while 1:
           if a==0 and b==0:
               break
           c=a%10
           d=b%10
           a=a//10
           b=b//10
           s+=c*d
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

