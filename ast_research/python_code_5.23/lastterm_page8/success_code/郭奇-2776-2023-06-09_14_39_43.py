def  myFun(a,b):
       n1=len(a)
       n2=len(b)
       r=0
       if n1==n2:
           
           for i in range(n1):
               r+=int(a[i])+int(b[i])
       else:
           c=n1-n2
           if c<0:
               c=-c
               for i in range(n1):
                   r+=int(a[i])+int(b[i+c])
           else:
               for i in range(n2):
                   r+=int(a[i+c])+int(b[i])
       return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

