def  myFun(a,b):
       if  a.isdigit()  and  b.isdigit():
           s=0
           a1=str(a)
           b1=str(b)
           c=min(a,b)
           for i in range(1,int(c)+1):
               s+=int(a1[-i])*int(b1[-i])
           return s
       else:
           return error
       
               

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

