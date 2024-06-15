def  myFun(a,b):
       if int(a)<=0 or int(b)<=0:
           return "error"
       else:
           c1=len(a)
           c2=len(b)
           if c1>c2:
               a=b[len(a)-len(b)+1::]
           elif c2>c1:
               b=b[len(b)-len(a)+1::]
           else:
               pass
           c=0
           for i in range(len(a)):
               c+=a[i]*b[i]
           return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

