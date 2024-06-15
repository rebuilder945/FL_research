def  myFun(a,b):
       c=len(a)
       d=len(c)
       f=min(c,d)
       g=0
       h=-1
       while f:
           g+=a[h]*b[h]
           f-=1
           h-=1
         
         

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

