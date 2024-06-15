def  myFun(a,b):
       if int(a) !=a or int(b)!=b or a<=0 or b<=0:
           return 'error'
       else:
           A=max(a,b)
           B=min(a,b)
           l = len(B)
           c=1
           for i in range(len(B)):
               c +=int(A[-i])*int(B[-i])
           return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

