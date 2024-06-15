def  myFun(a,b):
       if int(a)>0 and int(b)>0:
           s=max(a,b)
           m=min(a,b)
           c=len(s)-len(m)
           ls=[[0 for i in range(len(s))]for j in range(2)]
           for i in range(len(ls)):
                       ls[0][i]=int(s[i])
           for i in range(len(m)):
                       ls[1][i+c]=int(m[i])
           f=0
           for i in range(len(s)):
               f+=ls[0][i]*ls[1][i]
           return f
       else:
           return error


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

