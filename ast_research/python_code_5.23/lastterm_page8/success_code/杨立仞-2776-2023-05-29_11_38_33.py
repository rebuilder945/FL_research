def  myFun(a,b):
       x=len(str(a))
       y=len(str(b))
       z=0
       if x<y:
           a=a[::-1]
           a=str(int(a)*10**(y-x))
           a=a[::-1]
           for i in range(y):
               z+=int(a[i])*int(b[i])
       elif x>=y:
           b=b[::-1]
           b=str(int(b)*10**(x-y))
           b=b[::-1]
           for j in range(x):
               z+=int(a[j])*int(b[i])
       return z


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

