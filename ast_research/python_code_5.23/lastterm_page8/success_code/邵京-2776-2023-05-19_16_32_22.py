def  myFun(a,b):
       x=len(str(a))
       y=len(str(b))
       z=0
       if x<y:
           a.reverse()
           a*=10**(y-x)
           a.reverse()
           for i in range(0,y):
               z+=int(a[i])*int(b[i])
       elif y<x:
           b.reverse()
           b*=10**(x-y)
           b.reverse()
           for i in range(0,x):
               z+=int(a[i])*int(b[i])
       else:
           for i in range(0,x):
               z+=int(a[i])*int(b[i])
       return z
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

