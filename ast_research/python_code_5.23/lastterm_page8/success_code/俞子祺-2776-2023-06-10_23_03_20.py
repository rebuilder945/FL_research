def  myFun(a,b):
       n=0
       m=0
       h=0
       j=0
       while a>0 and b>0:
           n=a%10
           m=b%10
           h=n+m
           j+=h
           a=a//10
           b=b//10
       return j

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

