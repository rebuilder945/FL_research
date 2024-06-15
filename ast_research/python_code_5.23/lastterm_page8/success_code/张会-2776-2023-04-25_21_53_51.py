def  myFun(a,b):
       s=[]
       if a==int(a) and b==int(b):
           a,b=max(a,b),min(a,b)
           a1=str(a)
           b1=str(b)
           x=len(a1)-len(b1)
           b2='0'*x+b1
           for i in range(len(a1)):
               y=eval(a1[i])*eval(b2[i])
               s.append(y)
           zonghe=sum(s)
           return zonghe
       else:
           return 'error'

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

